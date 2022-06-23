import app
import unittest


class OneTest (unittest.TestCase):

    def test_app_one(self):
        self.assertEqual(app.dataa + app.datab, 300, "expecting 350")

    def test_app_two(self):
        self.assertEqual(app.dataa + app.datab, 300, "expecting 300")

    def test_app_three(self):
        "this test is conducted to validate the important parameters"
        self.assertEqual(app.dataa + app.datab, 300, "expecting 300")
        print("test three -->", self.shortDescription())


if __name__ == '__main__':
    unittest.main()
