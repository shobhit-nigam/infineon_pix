import app
import unittest

class OneTest (unittest.TestCase):
    def test_app_one(self):
        self.assertEqual(app.add(3,4), 6, "expecting 6")

    def test_app_two(self):
        self.assertEqual(app.add(3,4), 7, "expecting 7")

unittest.main()
