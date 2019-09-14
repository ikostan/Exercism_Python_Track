
ERROR = 'ERROR: number should be between 1 and 64 (inclusive).'


def square(number):
    """
    Calculates how many grains were on each square
    :param number:
    :return:
    """

    if number <= 0 or not number or number > 64:
        raise ValueError(ERROR)

    return 2**(number - 1)


def total(number):
    """
    Calculates the total number of grains
    :param number:
    :return:
    """
    if number <= 0 or not number or number > 64:
        raise ValueError(ERROR)

    return 2 ** number - 1
