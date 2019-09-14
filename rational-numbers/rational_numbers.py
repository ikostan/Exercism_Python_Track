from __future__ import division


class Rational:
    """
    A rational number is defined as the quotient of two integers a and b,
    called the numerator and denominator, respectively, where b != 0.
    """

    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError('ERROR: denominator can not be zero')
        elif numer == 0:
            self.numer = numer
            self.denom = denom
        else:
            if (numer > 0 and denom > 0) or (numer < 0 and denom < 0):
                self.numer = abs(int(numer / gcd(numer, denom)))
            else:
                self.numer = abs(int(numer / gcd(numer, denom))) * (-1)
            self.denom = abs(int(denom / gcd(numer, denom)))

    def __eq__(self, other):
        if self.numer != 0:
            return self.numer == other.numer and self.denom == other.denom
        else:
            return self.numer == other.numer

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
        if self.denom * other.numer != 0:
            return Rational((self.numer * other.denom),
                            (self.denom * other.numer))
        else:
            raise ValueError('ERROR: denominator can not be zero')

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
        # to a non-negative integer power n is r^n = (a^n)/(b^n).
        if power >= 0 and type(power) == int:
            return Rational((self.numer ** power),
                            (self.denom ** power))
        # Exponentiation of a rational number r = a/b
        # to a negative integer power n is r^n = (b^m)/(a^m), where m = |n|.
        elif power < 0 and type(power) == int:
            return Rational((self.denom ** abs(power)),
                            (self.numer ** abs(power)))
        # Exponentiation of a rational number r = a/b to a
        # real (floating-point) number x is
        # the quotient (a^x)/(b^x), which is a real number.
        elif power >= 0 and type(power) == float:
            return Rational((self.numer ** power),
                            (self.denom ** power))
        # Exponentiation of a rational number r = a/b to a
        # negative real (floating-point) number x is
        # the quotient (a^x)/(b^x), which is a real number.
        elif power < 0 and type(power) == float:
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


def gcd(numer: int, denom: int):
    """
    Finds greatest common divisor (gcd).
    :param numer:
    :param denom:
    :return:
    """

    if numer == 0:
        return 0

    if numer == denom:
        return denom

    divisor = min(abs(numer), abs(denom))
    while not (numer % divisor == 0 and denom % divisor == 0):
        divisor -= 1
        # print('gcd: {}'.format(divisor))  # debug only

    return divisor
