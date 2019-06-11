def is_pangram(sentence:str):
    '''
    A pangram is a sentence using every letter of the alphabet at least once.
    The best known English pangram is:
            The quick brown fox jumps over the lazy dog.
    :param sentence:
    :return:
    '''
    import string
    letters = string.ascii_lowercase
    sentence = sentence.lower()

    for c in letters:
        if c not in sentence:
            return False

    return True
