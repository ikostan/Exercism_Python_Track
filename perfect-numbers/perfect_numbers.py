def classify(number):
    """
    Determine if a number is perfect, abundant, or deficient
    based on Nicomachus' (60 - 120 CE) classification scheme for natural numbers.

    Categories of perfect, abundant, or deficient based on their aliquot sum.

    The aliquot sum is defined as the sum of the factors of a number not including the number itself.
    For example, the aliquot sum of 15 is (1 + 3 + 5) = 9

    :param number:
    :return:
    """

    if number < 1:
        raise ValueError("Error: Invalid input")

    if number == 1:
        return 'deficient'

    aliquot_sum = sum(get_factors(number))

    # Perfect: aliquot sum = number
    if aliquot_sum == number:
        return 'perfect'

    # Abundant: aliquot sum > number
    if aliquot_sum > number:
        return 'abundant'

    # Deficient: aliquot sum < number
    if aliquot_sum < number:
        return 'deficient'


def get_factors(number):
    """
    Returns all possible factors
    :param number:
    :return:
    """
    import math
    factors = set()

    # efficient way of finding all the factors of a number in Python
    for n in range(1, int(math.sqrt(number)) + 1):
        if number % n == 0:
            factors.add(n)
            # the factors of a number not including the number itself
            if n != 1:
                factors.add(number//n)

    return factors
