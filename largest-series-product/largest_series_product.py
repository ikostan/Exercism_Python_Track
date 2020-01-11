def largest_product(series: str, size: int) -> int:
    """
    Given a string of digits, calculate the largest
    product for a contiguous substring of digits of length n.
    :param series:
    :param size:
    :return:
    """

    if len(series) < size or size < 0:
        raise ValueError('ERROR: illegal string.')

    if series == '':
        return 1

    largest = 0
    for n in range(0, len(series)):
        if n + size <= len(series):
            temp = multiply_list_members(series[n: n + size])
            if largest < temp:
                largest = temp
        else:
            break

    return largest


def multiply_list_members(series: str) -> int:
    """
    Multiply all numbers in the list
    :param series:
    :return:
    """
    result = 1
    for char in series:
        result *= int(char)
    return result

