def square_of_sum(number):
    number = list(range(1, number + 1))
    return sum(number) ** 2


def sum_of_squares(number):
    number = list(range(1, number + 1))
    return sum([(n ** 2) for n in number])


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
