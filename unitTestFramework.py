import unittest
import os

class unitTestFramework(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
        print("inside test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(),['hello','world'])


if __name__ == "__main__":
    unittest.main()
