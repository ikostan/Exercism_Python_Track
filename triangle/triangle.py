def equilateral(sides):
    '''
    An equilateral triangle has all three sides the same length.
    :param sides:
    :return:
    '''

    if not is_valid(sides):
        return False

    if len(set(sides)) > 1:
        return False

    return True


def isosceles(sides):
    '''
    An isosceles triangle has at least two sides the same length.
    (It is sometimes specified as having exactly two sides the same length,
    but for the purposes of this exercise we'll say at least two.)
    :param sides:
    :return:
    '''

    if not is_valid(sides):
        return False

    if len(set(sides)) > 2:
        return False

    return True


def scalene(sides):
    '''
    A scalene triangle has all sides of different lengths.
    :param sides:
    :return:
    '''

    if not is_valid(sides):
        return False

    if len(set(sides)) < 3:
        return False

    return True


def is_valid(sides):
    '''
    For a shape to be a triangle at all, all sides have to be of length > 0,
    and the sum of the lengths of any two sides must be greater than or equal
    to the length of the third side.
    :param sides:
    :return:
    '''

    # 1 - all sides have to be of length > 0:
    if sum(sides) <= 0:
        return False

    # 2 - the sum of the lengths of any two sides must be greater than or equal
    # to the length of the third side:
    if sides[0] + sides[1] < sides[2]:
        return False

    if sides[2] + sides[1] < sides[0]:
        return False

    if sides[0] + sides[2] < sides[1]:
        return False

    return True

