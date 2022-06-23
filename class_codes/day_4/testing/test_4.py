import app
import unittest

class OneTest (unittest.TestCase):
    def test_app_one(self):
        self.assertEqual(app.add(2,4), 6, "expecting 6")

    def test_app_two(self):
        self.assertEqual(app.add(3,4), 7, "expecting 7")

    def funca(self):
        self.assertEqual(app.add(3,4), 8, "expecting 7")

if __name__ == '__main__':
    unittest.main()
