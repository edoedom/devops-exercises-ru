import unittest
from app.main import create_app


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["resources"]["users"], "/users")

    def test_users_projection_and_order(self):
        response = self.app.get("/users")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(list(data), sorted(data))
        for user in data.values():
            self.assertEqual(set(user), {"name", "description"})

    def test_existing_user(self):
        response = self.app.get("/users/geralt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Geralt of Rivia")
        self.assertNotIn("id", response.json)

    def test_missing_user(self):
        self.assertEqual(self.app.get("/users/nobody").status_code, 404)

    def test_unimplemented_endpoint(self):
        self.assertEqual(self.app.get("/users/geralt/something").status_code, 501)


if __name__ == "__main__":
    unittest.main()
