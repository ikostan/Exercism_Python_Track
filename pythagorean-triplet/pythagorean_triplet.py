"""
Given an input integer N, find all Pythagorean triplets
for which a + b + c = N.

For example, with N = 1000, there is exactly one Pythagorean triplet
for which a + b + c = 1000: {200, 375, 425}.
"""

import math


def triplets_with_sum(number) -> set:
    """
    Given an input integer N,
    find all Pythagorean triplets for which:
    a + b + c = N.

    :param number:
    :return:
    """

    return set(t for t in triplets_in_range(int(math.sqrt(number)),
                                            number)
               if sum(t) == number)


def triplets_in_range(start: int, end: int) -> list:
    """
    Returns all possible triplets within specific range

    :param start:
    :param end:
    :return:
    """

    triplets = []

    for b in range(end//4, end//2):
        for a in range(start, b):
            # calculate c
            c = int(math.sqrt(b ** 2 + a ** 2))
            # check is a, b, c Pythagorean triplet
            if is_triplet([a, b, c]):
                triplets.append((a, b, c))

    return triplets


def is_triplet(triplet: list) -> bool:
    """
    A Pythagorean triplet is a set of three natural numbers:
    {a, b, c}
    for which:
    a**2 + b**2 = c**2
    and such that:
    a < b < c

    :param triplet:
    :return:
    """

    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[-1] ** 2
