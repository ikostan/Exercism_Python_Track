import math


def primes(limit: int) -> list:
    """
    Sieve of Eratosthenes:
    A simple, ancient algorithm for finding all prime numbers
    up to any given limit. It does so by iteratively marking
    as composite (i.e. not prime) the multiples of each prime,
    starting with the multiples of 2. It does not use any
    division or remainder operation.
    :param limit:
    :return:
    """

    if limit < 2:
        return []

    numbers = [i for i in range(1, limit + 1)]
    numbers[0] = False

    for index, number in enumerate(numbers):
        if number:
            for i in range(2, number):
                if number % i == 0:
                    numbers[index] = False

    return [i for i in numbers if i]
