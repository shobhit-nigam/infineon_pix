import app
import unittest

class OneTest (unittest.TestCase):
    def test_app_one(self):
        self.assertRegex("date is 23, day is Thu", "\d+", "was looking for a number")

    def test_app_two(self):
        self.assertRegex("date is 23, day is Thu", "hello", "was looking for hello")

if __name__ == '__main__':
    unittest.main()
