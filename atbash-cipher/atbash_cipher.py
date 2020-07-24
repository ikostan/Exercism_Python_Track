import string

LOWERCASE = string.ascii_lowercase
DIGITS = string.digits


def replace_char(char: str) -> str:
    if char.isalpha():
        return LOWERCASE[len(LOWERCASE) - LOWERCASE.index(char) - 1]
    return char


def encode(plain_text: str) -> str:
    """
    The Atbash cipher is a simple substitution cipher that
    relies on transposing all the letters in the alphabet
    such that the resulting alphabet is backwards. The first
    letter is replaced with the last letter, the second with
    the second-last, and so on.

    :param plain_text:
    :return: substitution cipher that relies on transposing
            all the letters in the alphabet
    """
    result: list = [replace_char(char) for char in plain_text.lower()
                    if char in LOWERCASE or char in DIGITS]

    counter = 0
    results = list()
    for char in result:
        results.append(char)
        counter += 1
        if counter == 5:
            counter = 0
            results.append(' ')
    return ''.join(results).strip()


def decode(ciphered_text: str) -> str:
    """
    Decode Atbash cipher

    :param ciphered_text: Atbash cipher
    :return: decoded text
    """
    return ''.join(replace_char(char) for char in ciphered_text
                   if char in LOWERCASE or char in DIGITS)
