def square_of_sum(number):
    '''
    The square of the sum of the first n natural numbers
    :param number:
    :return:
    '''
    number = list(range(1, number + 1))
    return sum(number) ** 2


def sum_of_squares(number):
    '''
    The sum of the squares of the first n natural numbers
    :param number:
    :return:
    '''
    number = list(range(1, number + 1))
    return sum([(n ** 2) for n in number])


def difference_of_squares(number):
    '''
    The difference between the square of the sum of the first n natural numbers
    and the sum of the squares of the first n natural numbers
    :param number:
    :return:
    '''
    return square_of_sum(number) - sum_of_squares(number)
