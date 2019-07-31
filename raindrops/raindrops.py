def convert(number: int):
    '''
    Convert a number to a string, the contents of which depend on the number's factors.

    If the number has 3 as a factor, output 'Pling'.
    If the number has 5 as a factor, output 'Plang'.
    If the number has 7 as a factor, output 'Plong'.

    :param number:
    :return:
    '''

    nub_str_converter = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    factors = find_factors(number)
    # If the number does not have 3, 5, or 7 as a factor, just pass the number's digits straight through.
    # print(type(factors))  # debug only
    if type(factors) != list:
        return str(factors)

    result = ''
    for f in factors:
        result += nub_str_converter[f]

    return result


def find_factors(number: int):
    '''
    If the number does not have 3, 5, or 7 as a factor, just pass the number's digits straight through.
    :param number:
    :return:
    '''

    results = []
    factors = [3, 5, 7]

    for f in factors:
        if number % f == 0:
            results.append(f)

    if results is None or results == []:
        return number

    return results
