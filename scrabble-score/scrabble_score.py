def score(word: str) -> int:
    """
    Given a word, compute the scrabble score for that word.

    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10

    :param word:
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

    total = 0
    for letter in word.upper():
        for key in letter_value:
            if letter in letter_value[key]:
                total += key
                break
    return total
