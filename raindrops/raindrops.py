nub_str_converter = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }


def convert(number: int) -> str:
    """
    Convert a number to a string, the contents of
    which depend on the number's factors.

    If the number has 3 as a factor, output 'Pling'.
    If the number has 5 as a factor, output 'Plang'.
    If the number has 7 as a factor, output 'Plong'.

    :param number:
    :return:
    """

    factors = find_factors(number)
    # If the number does not have 3, 5, or 7 as a factor,
    # just pass the number's digits straight through.
    # print(type(factors))  # debug only
    if factors is None:
        return str(number)

    result = ''
    for f in factors:
        result += nub_str_converter[f]

    return result


def find_factors(number: int):
    """
    Checks if number has factors: 3, 5, 7
    If the number does not have any factors, returns number straight through.
    :param number:
    :return:
    """

    results = []

    for f in nub_str_converter.keys():
        if number % f == 0:
            results.append(f)

    if not results:
        return None

    return results
