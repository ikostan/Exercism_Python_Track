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

    clean_string = ''.join(char.lower()
                           for char in string
                           if char not in [' ', '-'])
    for char in clean_string:
        if clean_string.count(char) > 1:
            return False
    return True
