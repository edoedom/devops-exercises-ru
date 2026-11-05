import unittest
from app.main import create_app


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_index(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_matrix(self):
        response = self.client.get("/matrix/123n456n789")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "1 2 3" + chr(10) + "4 5 6" + chr(10) + "7 8 9")

    def test_column_and_row(self):
        self.assertEqual(self.client.get("/columns/123n456n789/2").text,
                         "2" + chr(10) + "5" + chr(10) + "8")
        self.assertEqual(self.client.get("/rows/123n456n789/1").text, "1 2 3")

    def test_invalid_matrix(self):
        for value in ["123n45", "123n4x6", "n123", "123n"]:
            with self.subTest(value=value):
                self.assertEqual(self.client.get("/matrix/" + value).status_code, 400)

    def test_invalid_index(self):
        self.assertEqual(self.client.get("/rows/123n456/0").status_code, 400)
        self.assertEqual(self.client.get("/columns/123n456/4").status_code, 400)


if __name__ == "__main__":
    unittest.main()
