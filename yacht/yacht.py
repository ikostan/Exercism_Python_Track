"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


def choice(dice: list):
    '''
    Sum of the dice
    :param dice:
    :return:
    '''

    return sum(dice)


def ones(dice: list):
    '''
    1 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(1) * 1


def twos(dice: list):
    '''
    2 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(2) * 2


def threes(dice: list):
    '''
    3 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(3) * 3


def fours(dice: list):
    '''
    4 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(4) * 4


def fives(dice: list):
    '''
    5 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(5) * 5


def sixes(dice: list):
    '''
    6 × number of ones
    :param dice:
    :return:
    '''

    return dice.count(6) * 6


def full_house(dice: list):
    '''
    Total of the dice: 3 3 3 5 5 scores 19
    :param dice:
    :return:
    '''

    if len(set(dice)) == 2:
        if len(set(sorted(dice)[:3])) == 1 and len(set(sorted(dice)[3:])) == 1:
            return sum(dice)
        if len(set(sorted(dice)[:2])) == 1 and len(set(sorted(dice)[2:])) == 1:
            return sum(dice)
    return 0


def four_of_a_kind(dice: list):
    '''
    Total of the four dice:  4 4 4 4 6 scores 16
    :param dice:
    :return:
    '''

    if 1 <= len(set(dice)) <= 2:
        return sum([t for t in dice if dice.count(t) >= 4][:4])
    return 0


def little_straight(dice: list):
    '''
    30 points: 1 2 3 4 5 -> scores 30
    :param dice:
    :return:
    '''

    if [1, 2, 3, 4, 5] == sorted(dice):
        return 30
    return 0


def big_straight(dice: list):
    '''
    30 points: 2 3 4 5 6 -> scores 30
    :param dice:
    :return:
    '''

    if [2, 3, 4, 5, 6] == sorted(dice):
        return 30
    return 0


def yacht(dice: list):
    '''
    50 points. Example: 4 4 4 4 4 scores 50
    :param dice:
    :return:
    '''

    if len(set(dice)) == 1:
        return 50
    return 0


# Score categories.
# Change the values as you see fit.
YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice


def score(dice, category):
    return category(dice)
