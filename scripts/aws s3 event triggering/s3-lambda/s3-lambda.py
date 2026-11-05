"""Уведомления S3 → Lambda → SNS; переменная TOPIC_ARN обязательна."""
import os
from urllib.parse import unquote_plus

_sns = None


def lambda_handler(event, context):
    global _sns
    if event.get("Event") == "s3:TestEvent":
        return {"processed": 0}
    if _sns is None:
        import boto3
        _sns = boto3.client("sns")
    count = 0
    for record in event.get("Records", []):
        if record.get("eventSource") != "aws:s3":
            continue
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        _sns.publish(TopicArn=os.environ["TOPIC_ARN"],
                     Subject="S3 object created",
                     Message=f"Object {key!r} was created in bucket {bucket!r}")
        count += 1
    return {"processed": count}
