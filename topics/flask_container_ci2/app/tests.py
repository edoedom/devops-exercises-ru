import unittest
from .main import create_app


class TestAppFactory(unittest.TestCase):
    def test_factory_has_routes(self):
        app = create_app()
        app.config["TESTING"] = True
        self.assertEqual(app.test_client().get("/").status_code, 200)
