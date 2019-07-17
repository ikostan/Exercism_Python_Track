def is_valid(isbn):
    '''
    Given a string the program will check if the provided string is a valid ISBN-10.
    :param isbn:
    :return:
    '''

    # ISBN is invalid in case input string is empty
    if not isbn or isbn == '':
        return False

    # Converting from strings to numbers
    digits = []
    for i in isbn:
        if i.isdigit():
            digits.append(int(i))

    # Check digit of an ISBN-10 may be 'X' (representing '10')
    if isbn[-1] == 'X':
        digits.append(10)

    # ISBN is invalid in case it has less than 10 digits
    if len(digits) < 10:
        return False

    # Multiply ISBN members:
    for n in range(10, 0, -1):
        digits[n - 1] *= n

    # Calculate mod and return the answer
    # If the result is 0, then it is a valid ISBN-10, otherwise it is invalid:
    return sum(digits) % 11 == 0
