import string


def score(word: str) -> int:
    """
    Given a word, computes the
    scrabble score for that word.
    :param word:
    :return:
    """

    total = 0
    scrabble_score_table = scrabble_score_generator()
    for letter in word.upper():
        total += scrabble_score_table[letter]
    return total


def scrabble_score_generator() -> dict:
    """
    Generates Scrabble Score table
    :return:
    """
    scrabble_score_table = dict()
    for char in string.ascii_uppercase:
        scrabble_score_table[char] = get_char_score(char)
    return scrabble_score_table


def get_char_score(char: str) -> int:
    """
    Returns Scrabble Score for requested char

    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10

    :param char:
    :return:
    """

    letter_value = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ',
    }

    for key in letter_value:
        if char in letter_value[key]:
            return key
