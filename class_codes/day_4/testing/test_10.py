import app
import unittest


class OneTest (unittest.TestCase):
    def test_app_one(self):
        self.assertEqual(app.dataa + app.datab, 350, "expecting 350")

if __name__ == '__main__':
    unittest.main()
