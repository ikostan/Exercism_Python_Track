import unittest
from leap import is_leap


class MyTestCase(unittest.TestCase):
    # 1997 is not a leap year
    def test_1997(self):
        self.assertEqual(False, is_leap(1997))

    # but 1996 is
    def test_1996(self):
        self.assertEqual(True, is_leap(1996))

    # 1900 is not a leap year
    def test_1900(self):
        self.assertEqual(False, is_leap(1900))

    # but 2000 is
    def test_2000(self):
        self.assertEqual(True, is_leap(2000))

    # 2001 is not a leap year
    def test_2001(self):
        self.assertEqual(False, is_leap(2001))


if __name__ == '__main__':
    unittest.main()
