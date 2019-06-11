import unittest
from leap import leap_year


class MyTestCase(unittest.TestCase):

    def test_year_not_divisible_by_4(self):
        self.assertIs(leap_year(2015), False)

    def test_year_divisible_by_2_not_divisible_by_4(self):
        self.assertIs(leap_year(1970), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(leap_year(2100), False)

    def test_year_divisible_by_400(self):
        self.assertIs(leap_year(2000), True)

    def test_year_divisible_by_200_not_divisible_by_400(self):
        self.assertIs(leap_year(1800), False)

    # 1997 is not a leap year
    def test_1997(self):
        self.assertEqual(False, leap_year(1997))

    # but 1996 is
    def test_1996(self):
        self.assertEqual(True, leap_year(1996))

    # 1900 is not a leap year
    def test_1900(self):
        self.assertEqual(False, leap_year(1900))

    # but 2000 is
    def test_2000(self):
        self.assertEqual(True, leap_year(2000))

    # 2001 is not a leap year
    def test_2001(self):
        self.assertEqual(False, leap_year(2001))


if __name__ == '__main__':
    unittest.main()
