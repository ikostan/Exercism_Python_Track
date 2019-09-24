from collections import Counter


def is_isogram(string) -> bool:
    """
    Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word
    or phrase without a repeating letter,
    however spaces and hyphens are allowed to appear multiple times.

    Examples of isograms:
        lumberjacks
        background
        downstream
        six-year-old

    The word isograms, however, is not an isogram,
    because the s repeats.

    :param string:
    :return:
    """

    counter = Counter(string.lower())

    # 1. spaces allowed to appear multiple times
    spaces = 0
    if ' ' in counter:
        spaces = counter[' '] - 1

    # 2. hyphens are allowed to appear multiple times
    hyphens = 0
    if '-' in counter:
        hyphens = counter['-'] - 1

    return len(string) == len(counter.items()) + spaces + hyphens
