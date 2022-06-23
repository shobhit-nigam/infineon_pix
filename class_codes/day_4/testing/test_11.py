import app
import unittest


class OneTest (unittest.TestCase):
    def setUp(self):
        app.datab = 250
        print("changing the value of app.datab")

    def test_app_one(self):
        self.assertEqual(app.dataa + app.datab, 350, "expecting 350")

    def tearDown(self):
        app.datab = 100
        print("resetting the value")

if __name__ == '__main__':
    unittest.main()
