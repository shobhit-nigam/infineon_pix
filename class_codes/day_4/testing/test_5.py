import app
import unittest

class OneTest (unittest.TestCase):
    def test_app_one(self):
        self.assertAlmostEqual(11/3, 3)

    def test_app_two(self):
        self.assertAlmostEqual(10/3, 3.333)

    def test_app_three(self):
        self.assertAlmostEqual(17/4, 4.249999999)
        # arg1, arg2, decimal places, message, delta

if __name__ == '__main__':
    unittest.main()
