from __future__ import division
from math import gcd


class Rational:
    """
    A rational number is defined as the quotient of two integers a and b,
    called the numerator and denominator, respectively, where b != 0.
    """

    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError('ERROR: denominator can not be zero')

        self.numer = abs(int(numer / gcd(numer, denom)))
        if not((numer > 0 and denom > 0) or (numer < 0 and denom < 0)):
            self.numer *= -1

        self.denom = abs(int(denom / gcd(numer, denom)))

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        """
        The sum of two rational numbers:
        a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2).
        :param other:
        :return:
        """

        return Rational((self.numer * other.denom + other.numer * self.denom),
                        (self.denom * other.denom))

    def __sub__(self, other):
        """
        The difference of two rational numbers:
        a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2).
        :param other:
        :return:
        """

        return Rational((self.numer * other.denom - other.numer * self.denom),
                        (self.denom * other.denom))

    def __mul__(self, other):
        """
        The product (multiplication) of two rational numbers
        (a1 * a2) / (b1 * b2).
        :param other:
        :return:
        """
        return Rational((self.numer * other.numer),
                        (self.denom * other.denom))

    def __truediv__(self, other):
        """
        Dividing a rational number is
        (a1 * b2) / (a2 * b1) if a2 * b1 is not zero.
        :param other:
        :return:
        """
        return Rational((self.numer * other.denom),
                        (self.denom * other.numer))

    def __abs__(self):
        return Rational(abs(self.numer),
                        abs(self.denom))

    def __pow__(self, power):
        """
        Exponentiation of a rational number
        :param power:
        :return:
        """
        # Exponentiation of a rational number r = a/b
        # to a non-negative power n is r^n = (a^n)/(b^n).
        if power >= 0:
            return Rational((self.numer ** power),
                            (self.denom ** power))
        # Exponentiation of a rational number r = a/b
        # to a negative power n is r^n = (b^m)/(a^m), where m = |n|.
        return Rational((self.denom ** abs(power)),
                        (self.numer ** abs(power)))

    def __rpow__(self, base):
        """
        Exponentiation of a real number x to a rational number
        r = a/b is x^(a/b) = root(x^a, b),
        where root(p, q) is the qth root of p.
        :param base:
        :return:
        """
        return (base ** self.numer) ** (1./self.denom)
