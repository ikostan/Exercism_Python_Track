def steps(number):
    '''
    The Collatz Conjecture or 3x+1 problem.
    Given a number n, return the number of steps required to reach 1.
    :param number:
    :return:
    '''

    # The Collatz Conjecture is only concerned with strictly positive integers,
    # so your solution should raise a ValueError with a meaningful
    # message if given 0 or a negative integer.
    if number <= 0:
        raise ValueError('.+')

    steps_total = 0
    while number != 1:
        # If n is even, divide n by 2 to get n / 2.
        if number % 2 == 0:
            number = number / 2
        else:
            # If n is odd, multiply n by 3 and add 1 to get 3n + 1.
            number = number * 3 + 1
        steps_total += 1

    return steps_total
