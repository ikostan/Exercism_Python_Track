import unittest
from rectangles import Rectangle


class RectangleTest(unittest.TestCase):
    def test_dots(self):
        rectangle = Rectangle(([4, 2], [2, 1], [2, 2], [4, 1]))
        self.assertListEqual(rectangle.A, [2, 1])
        self.assertListEqual(rectangle.B, [2, 2])
        self.assertListEqual(rectangle.C, [4, 1])
        self.assertListEqual(rectangle.D, [4, 2])

    def test_equal(self):
        rectangle_a = Rectangle(([4, 2], [2, 1], [2, 2], [4, 1]))
        rectangle_b = Rectangle(([2, 2], [4, 1], [4, 2], [2, 1]))
        self.assertTrue(rectangle_a == rectangle_b)

    def test_not_equal(self):
        rectangle_a = Rectangle(([4, 2], [2, 1], [2, 2], [4, 1]))
        rectangle_b = Rectangle(([4, 2], [2, 2], [4, 4], [2, 4]))
        self.assertFalse(rectangle_a == rectangle_b)
