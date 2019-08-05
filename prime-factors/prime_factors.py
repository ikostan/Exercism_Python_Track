import math


def factors(value: int):
    '''
    Compute the prime factors of a given natural number.
    Note that 1 is not a prime number.

    Example:
        What are the prime factors of 60?
        2 * 2 * 3 * 5 = 4 * 15 = 60

    :param value:
    :return:
    '''

    primes = []
    n = 2  # initial divisor

    if value == 1:
        return primes

    while not is_done(value, primes):

        if is_prime(n):
            if value % n == 0:
                v = value
                while v % n == 0:
                    v = v / n
                    primes.append(n)
                    # Check if multiplication of all primes in list == value:
                    if is_done(value, primes):
                        return primes
        n += 1

    return primes


def is_done(value: int, primes: list):
    '''
    Check if multiplication of all primes in list == value.

    :param value:
    :param primes:
    :return:
    '''

    if not primes or len(primes) == 0:
        return False

    n = 1
    for p in primes:
        n *= p

    return n == value


def is_prime(num: int):
    '''
    A prime number is only evenly divisible by itself and 1.
    Test if number is prime.

    :param num:
    :return:
    '''

    if num == 1:
        return False

    if num == 2:
        return True

    if num != 2 and num % 2 == 0:
        return False

    for n in range(3, int(math.sqrt(num)) + 1, 2):

        if num % n == 0 and n != num:
            return False

    return True
