# A Python program to print all
# combinations of given length
from itertools import combinations


class Rectangle:
    """
    A---B
    |   |
    C---D
    """

    def __init__(self, dots: tuple):
        self.D: list = max(dots)
        self.A: list = min(dots)
        self.B: list = self.__find_b(dots)
        self.C: list = self.__find_c(dots)

    def __find_b(self, dots: tuple) -> list:
        for dot in dots:
            if self.A[0] == dot[0] and \
                    self.A[1] < dot[1] and \
                    self.D[1] == dot[1]:
                return dot

    def __find_c(self, dots: tuple) -> list:
        for dot in dots:
            if self.D[0] == dot[0] and \
                    self.D[1] > dot[1] and \
                    self.A[1] == dot[1]:
                return dot

    def __eq__(self, other):
        return self.A == other.A and \
               self.B == other.B and \
               self.C == other.C and \
               self.D == other.D

    @staticmethod
    def is_rectangle(dots: tuple, strings: list) -> bool:
        if len(dots) != 4:
            return False

        rec = list()
        D: list = max(dots)
        A: list = min(dots)
        if A[0] == D[0] or A[1] == D[1]:
            return False

        rec.append(D)
        rec.append(A)

        # find B
        for dot in dots:
            if A[0] == dot[0] and \
                    A[1] < dot[1] and \
                    D[1] == dot[1] and \
                    dot not in rec:
                B = dot
                rec.append(dot)

        # find C
        for dot in dots:
            if D[0] == dot[0] and \
                    D[1] > dot[1] and \
                    A[1] == dot[1] and \
                    dot not in rec:
                C = dot
                rec.append(dot)

        # true rectangle has 4 corners/dots only
        if len(rec) != 4:
            return False

        # vertical lines should be consist of '+'/'|' only
        for row in strings[A[0] + 1: C[0]]:
            if row[A[1]] == ' ' or \
                    row[B[1]] == ' ' or \
                    row[A[1]] == '-' or \
                    row[B[1]] == '-':
                return False

        # horizontal line should be consist of '+'/'-' only
        for c in strings[A[0]][A[1]: B[1]]:
            if c == ' ':
                return False

        # horizontal line should be consist of '+'/'-' only
        for d in strings[C[0]][C[1]: D[1]]:
            if d == ' ':
                return False

        return True


def rectangles(strings: list) -> int:
    """
    Count the rectangles in an ASCII diagram

    :param strings: ASCII diagram
    :return: rectangles counter
    """

    all_rectangles = list()
    # get all coordinates for possible rectangle angle/dot (dot == '+')
    all_dots = list()
    for i_row, row in enumerate(strings):
        for i_col, col in enumerate(row):
            if col == '+':
                all_dots.append([i_row, i_col])

    # get all possible combinations of 4 dots
    comb = combinations(all_dots, 4)

    # check if combination is true rectangle
    for c in comb:
        flag = Rectangle.is_rectangle(c, strings)
        if flag:
            r = Rectangle(c)
            if r not in all_rectangles:
                all_rectangles.append(r)

    # count total rectangles and return the number
    return len(all_rectangles)
