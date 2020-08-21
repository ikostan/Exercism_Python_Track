import string

LETTERS = string.ascii_uppercase


def rows(letter: str) -> list:
    """
    The diamond kata takes as its input a letter, and outputs
    it in a diamond shape. Given a letter, it prints a diamond
    starting with 'A', with the supplied letter at the widest point.

    :param letter:
    :return:
    """

    diamond: list = list()

    for i, char in enumerate(LETTERS[:LETTERS.index(letter) + 1]):

        temp_row = [' ' for i in range((LETTERS.index(letter) * 2) + 1)]
        if i == 0:
            temp_row[int(len(temp_row) / 2)] = char
        else:
            temp_row[int(len(temp_row) / 2) - i] = char
            temp_row[int(len(temp_row) / 2) + i] = char

        diamond.append(''.join(temp_row))

    r_diamond = [d for d in diamond][:-1]
    r_diamond.reverse()

    return diamond + r_diamond
