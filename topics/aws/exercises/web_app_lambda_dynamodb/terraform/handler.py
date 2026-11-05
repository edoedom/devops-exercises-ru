"""API Gateway payload 2.0; AWS credentials предоставляет execution role."""
import base64
import binascii
import json
import logging
import os

_table = None
log = logging.getLogger(__name__)


def get_table():
    global _table
    if _table is None:
        import boto3
        _table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
    return _table


def response(status, body):
    return {"statusCode": status, "headers": {"content-type": "application/json"},
            "body": json.dumps(body)}


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")
    user_id = (event.get("pathParameters") or {}).get("id")
    if not isinstance(user_id, str) or not user_id or len(user_id) > 200:
        return response(400, {"error": "invalid id"})
    if method not in ("GET", "PUT"):
        return response(405, {"error": "method not allowed"})
    if method == "PUT":
        try:
            body = event.get("body") or ""
            if event.get("isBase64Encoded"):
                body = base64.b64decode(body, validate=True).decode("utf-8")
            if len(body) > 4096:
                return response(400, {"error": "body is too large"})
            data = json.loads(body)
            login = data.get("login") if isinstance(data, dict) else None
            if not isinstance(login, str) or not login.strip() or len(login) > 100:
                return response(400, {"error": "invalid login"})
        except (ValueError, TypeError, UnicodeError, binascii.Error):
            return response(400, {"error": "invalid JSON body"})
    try:
        table = get_table()
        if method == "PUT":
            item = {"id": user_id, "login": login}
            table.put_item(Item=item)
            return response(200, item)
        item = table.get_item(Key={"id": user_id}, ConsistentRead=True).get("Item")
        return response(200, item) if item else response(404, {"error": "not found"})
    except Exception:
        log.exception("DynamoDB request failed")
        return response(500, {"error": "internal error"})
