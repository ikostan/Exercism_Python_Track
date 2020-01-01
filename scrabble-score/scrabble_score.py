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

    letter_value = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ',
    }

    scrabble_score_table = dict()
    for letter_score in letter_value.keys():
        for letter in letter_value[letter_score]:
            scrabble_score_table[letter] = letter_score
    return scrabble_score_table
