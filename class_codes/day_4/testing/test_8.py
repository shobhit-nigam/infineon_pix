import app
import unittest

dataa = 100
datab = 200

class OneTest (unittest.TestCase):
    @unittest.skipIf(dataa < datab, "will skip")
    def test_app_one(self):
        self.assertRegex("date is, day is Thu", "\d+", "was looking for a number")

    @unittest.expectedFailure
    def test_app_two(self):
        self.assertRegex("date is, day is Thu", "\d+", "was looking for hello")

if __name__ == '__main__':
    unittest.main()
