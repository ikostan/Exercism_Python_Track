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

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 1
EQUAL = 0
UNEQUAL = -1


def sublist(list_one: list, list_two: list) -> int:
    if list_one == list_two:
        return EQUAL
    elif len(list_one) < len(list_two):
        if len(list_one) == 0:
            return SUBLIST

        indices = [i for i, n in enumerate(list_two) if list_two[i] == list_one[0]]
        for index in indices:
            if list_two[index: index + len(list_one)] == list_one:
                return SUBLIST
    elif len(list_two) < len(list_one):
        if len(list_two) == 0:
            return SUPERLIST

        indices = [i for i, n in enumerate(list_one) if list_one[i] == list_two[0]]
        for index in indices:
            if list_one[index: index + len(list_two)] == list_two:
                return SUPERLIST
    return UNEQUAL
