def abbreviate(words: str) -> str:
    """
    Convert a phrase to its acronym.

    Techies love their TLA (Three Letter Acronyms)!

    Help generate some jargon by writing a program
    that converts a long name like Portable Network
    Graphics to its acronym (PNG).
    :param words:
    :return:
    """

    return ''.join(word[0].upper() for word in clean_up_words(words))


def clean_up_words(words: str) -> list:
    """
    Remove garbage from words
    and return them as a list
    :param words:
    :return:
    """

    results = list()

    for w in words.split(' '):
        if '-' in w:
            w_split = w.replace('-', ' ').split(' ')
            for w_s in w_split:
                add_word(w_s, results)
        elif '_' in w:
            w = w.replace('_', '')
            add_word(w, results)
        else:
            add_word(w, results)

    return results


def add_word(word: str, results: list) -> None:
    """
    Checks for empty strings before adding word to a list
    :param word:
    :param results:
    :return:
    """
    if word != '':
        results.append(word)