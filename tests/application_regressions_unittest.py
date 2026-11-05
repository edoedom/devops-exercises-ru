"""Регрессии обработчиков без AWS credentials и сетевых запросов."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LambdaTests(unittest.TestCase):
    def setUp(self):
        self.module = load("users_handler", "topics/aws/exercises/web_app_lambda_dynamodb/terraform/handler.py")
        self.module._table = Mock()

    def event(self, method, body=None):
        return {"requestContext": {"http": {"method": method}},
                "pathParameters": {"id": "123"}, "body": body}

    def test_put_and_get(self):
        response = self.module.lambda_handler(self.event("PUT", '{"login":"alice"}'), None)
        self.assertEqual(response["statusCode"], 200)
        self.module._table.put_item.assert_called_once_with(Item={"id": "123", "login": "alice"})
        self.module._table.get_item.return_value = {"Item": {"id": "123", "login": "alice"}}
        result = self.module.lambda_handler(self.event("GET"), None)
        self.assertEqual(json.loads(result["body"])["login"], "alice")
        self.module._table.get_item.assert_called_once_with(Key={"id": "123"}, ConsistentRead=True)

    def test_bad_input(self):
        for body in ['{', '[]', '{}', '{"login":1}', '{"login":""}', '{"login":" "}']:
            self.assertEqual(self.module.lambda_handler(self.event("PUT", body), None)["statusCode"], 400)
        event = self.event("PUT", "not-base64!"); event["isBase64Encoded"] = True
        self.assertEqual(self.module.lambda_handler(event, None)["statusCode"], 400)
        self.module._table.put_item.assert_not_called()

    def test_missing_and_method(self):
        self.module._table.get_item.return_value = {}
        self.assertEqual(self.module.lambda_handler(self.event("GET"), None)["statusCode"], 404)
        self.assertEqual(self.module.lambda_handler(self.event("POST"), None)["statusCode"], 405)


class EventTests(unittest.TestCase):
    def test_all_records_and_key_decoding(self):
        handler = load("s3_handler", "scripts/aws s3 event triggering/s3-lambda/s3-lambda.py")
        handler._sns = Mock()
        records = [{"eventSource": "aws:s3", "s3": {"bucket": {"name": "lab"},
                    "object": {"key": key}}} for key in ["hello+world.txt", "a%2Fb.txt"]]
        with patch.dict("os.environ", {"TOPIC_ARN": "test-topic"}):
            self.assertEqual(handler.lambda_handler({"Records": records}, None), {"processed": 2})
        self.assertEqual(handler._sns.publish.call_count, 2)
        self.assertIn("a/b.txt", handler._sns.publish.call_args.kwargs["Message"])
        self.assertEqual(handler.lambda_handler({"Event": "s3:TestEvent"}, None), {"processed": 0})
