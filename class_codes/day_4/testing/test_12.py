import app
import unittest


class OneTest (unittest.TestCase):
    def setUp(self):
        print("calling setUp")

    @classmethod
    def setUpClass(cls):
        print('calling setup class')

    def test_app_one(self):
        self.assertEqual(app.dataa + app.datab, 300, "expecting 350")

    def test_app_two(self):
        self.assertEqual(app.dataa + app.datab, 300, "expecting 300")

    def test_app_three(self):
        self.assertEqual(app.dataa + app.datab, 300, "expecting 300")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDown class")

if __name__ == '__main__':
    unittest.main()
