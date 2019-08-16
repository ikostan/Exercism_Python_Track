def is_isogram(string) -> bool:
    """
    Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter,
    however spaces and hyphens are allowed to appear multiple times.

    Examples of isograms:
        lumberjacks
        background
        downstream
        six-year-old

    The word isograms, however, is not an isogram, because the s repeats.

    :param string:
    :return:
    """

    counter = 0

    # 1. spaces allowed to appear multiple times
    counter += string.count(' ')

    # 2. hyphens are allowed to appear multiple times
    counter += string.count('-')

    # 3. No repeating letters
    unique_letters_only = set([char.lower() for char in string if char.isalpha()])
    counter += len(unique_letters_only)

    return counter == len(string)
