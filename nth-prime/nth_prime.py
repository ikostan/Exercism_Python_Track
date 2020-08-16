import math


def prime(number: int) -> int:
    if number == 0:
        raise ValueError("ERROR: there is no zeroth prime!")

    primes: list = list()
    n = 1
    while len(primes) < number:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes[-1]


def is_prime(i: int):
    """
    Return TRUE if i is prime number. False otherwise
    :param i:
    :return:
    """

    if i == 1:
        return False

    if i == 2:
        return True

    if i > 2 and i % 2 == 0:
        return False

    for n in range(3, int(math.sqrt(i)) + 1, 2):
        if i % n == 0:
            return False

    return True
