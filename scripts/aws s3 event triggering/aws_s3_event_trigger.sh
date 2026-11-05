#!/usr/bin/env bash
# Учебный проект: создаёт новые ресурсы и email subscription; не запускается в CI.
set -euo pipefail
: "${AWS_REGION:?Set AWS_REGION}"
: "${EMAIL_ADDRESS:?Set your notification email}"
export AWS_DEFAULT_REGION="$AWS_REGION"
for tool in aws jq zip python3; do command -v "$tool" >/dev/null; done
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf -- "$work_dir"' EXIT
suffix="$(python3 -c 'import uuid; print(uuid.uuid4().hex[:16])')"
lab_name="devops-s3-$suffix"
bucket="$lab_name"
role="$lab_name"
account="$(aws sts get-caller-identity --query Account --output text)"
partition="$(aws sts get-caller-identity --query Arn --output text | cut -d: -f2)"
if [[ "$AWS_REGION" == us-east-1 ]]; then
  aws s3api create-bucket --bucket "$bucket" >/dev/null
else
  aws s3api create-bucket --bucket "$bucket"     --create-bucket-configuration "LocationConstraint=$AWS_REGION" >/dev/null
fi
# Весь дальнейший вывод помогает вручную удалить частично созданную лабораторию.
printf 'LAB=%s\nBUCKET=%s\nROLE=%s\nREGION=%s\n' "$lab_name" "$bucket" "$role" "$AWS_REGION"
aws s3api put-public-access-block --bucket "$bucket" --public-access-block-configuration   BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
topic="$(aws sns create-topic --name "$lab_name" --query TopicArn --output text)"
printf 'TOPIC_ARN=%s\n' "$topic"
aws sns subscribe --topic-arn "$topic" --protocol email --notification-endpoint "$EMAIL_ADDRESS"
jq -n '{Version:"2012-10-17",Statement:[{Effect:"Allow",Principal:{Service:"lambda.amazonaws.com"},Action:"sts:AssumeRole"}]}' > "$work_dir/trust.json"
role_arn="$(aws iam create-role --role-name "$role" --assume-role-policy-document "file://$work_dir/trust.json" --query Role.Arn --output text)"
log_group="/aws/lambda/$lab_name"
aws logs create-log-group --log-group-name "$log_group"
aws logs put-retention-policy --log-group-name "$log_group" --retention-in-days 7
log_arn="arn:$partition:logs:$AWS_REGION:$account:log-group:$log_group:*"
jq -n --arg topic "$topic" --arg logs "$log_arn"   '{Version:"2012-10-17",Statement:[{Effect:"Allow",Action:"sns:Publish",Resource:$topic},{Effect:"Allow",Action:["logs:CreateLogStream","logs:PutLogEvents"],Resource:$logs}]}' > "$work_dir/policy.json"
aws iam put-role-policy --role-name "$role" --policy-name lab-permissions --policy-document "file://$work_dir/policy.json"
cp "$script_dir/s3-lambda/s3-lambda.py" "$work_dir/handler.py"
(cd "$work_dir" && zip -q lambda.zip handler.py)
jq -n --arg topic "$topic" '{Variables:{TOPIC_ARN:$topic}}' > "$work_dir/env.json"
created=false
for attempt in 1 2 3 4 5 6; do
  if aws lambda create-function --function-name "$lab_name" --runtime python3.13     --handler handler.lambda_handler --memory-size 128 --timeout 30 --role "$role_arn"     --zip-file "fileb://$work_dir/lambda.zip" --environment "file://$work_dir/env.json"     > "$work_dir/function.json" 2> "$work_dir/create-error"; then
    created=true; break
  fi
  # Повторяем только ожидаемую задержку распространения IAM роли.
  if ! grep -q 'cannot be assumed by Lambda' "$work_dir/create-error"; then
    cat "$work_dir/create-error" >&2; exit 1
  fi
  sleep 5
done
if [[ "$created" != true ]]; then cat "$work_dir/create-error" >&2; exit 1; fi
aws lambda wait function-active-v2 --function-name "$lab_name"
function_arn="$(jq -r .FunctionArn "$work_dir/function.json")"
printf 'FUNCTION=%s\nLOG_GROUP=%s\n' "$lab_name" "$log_group"
aws lambda add-permission --function-name "$lab_name" --statement-id s3-invoke   --action lambda:InvokeFunction --principal s3.amazonaws.com   --source-arn "arn:$partition:s3:::$bucket" --source-account "$account" >/dev/null
jq -n --arg arn "$function_arn" '{LambdaFunctionConfigurations:[{LambdaFunctionArn:$arn,Events:["s3:ObjectCreated:*"]}]}' > "$work_dir/notifications.json"
# Это новый отдельный бакет; существующие настройки чужих бакетов не заменяются.
aws s3api put-bucket-notification-configuration --bucket "$bucket"   --notification-configuration "file://$work_dir/notifications.json"
printf 'Confirm the SNS subscription email, then upload a test object:\n'
printf 'aws s3 cp example.txt s3://%s/example.txt --region %s\n' "$bucket" "$AWS_REGION"
