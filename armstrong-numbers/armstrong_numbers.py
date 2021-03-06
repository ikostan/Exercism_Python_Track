import ast


def is_armstrong_number(number):
    """
    Armstrong number is a number that is equal
    to the sum of cubes of its digits.
    For example 0, 1, 153, 370, 371
    and 407 are the Armstrong numbers.
    Source: https://www.javatpoint.com/armstrong-number-in-c

    :param number:
    :return:
    """
    power = len(str(number))
    string_form = ' + '.join([str((int(n) ** power)) for n in str(number)])
    return number == ast.literal_eval(string_form)
