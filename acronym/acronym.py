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
            w = w.replace('-', ' ').split(' ')
            if w[0] != '':
                results.append(w[0])
            if w[1] != '':
                results.append(w[1])
        elif '_' in w:
            w = w.replace('_', '')
            if w != '':
                results.append(w)
        else:
            if w != '':
                results.append(w)

    return results
