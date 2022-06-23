import app
import unittest

class OneTest (unittest.TestCase):
    @unittest.skip("will skip")
    def test_app_one(self):
        self.assertRegex("date is, day is Thu", "\d+", "was looking for a number")

    def test_app_two(self):
        self.assertRegex("date is, day is Thu", "\d+", "was looking for hello")

if __name__ == '__main__':
    unittest.main()
