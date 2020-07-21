import string


UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase


def rotate(text: str, key: int) -> str:
    """
    Implementation of the rotational cipher, also sometimes called the Caesar cipher.

    :param text: input text
    :param key: key between 0 and 26
    :return: ROT text is written out in the same formatting
             as the input including spaces and punctuation.
    """
    result: list = list()
    for char in text:
        if char.isalpha():
            result.append(cipher_char(char, key))
        else:
            result.append(char)

    return ''.join(result)


def get_id(char: str, key: int) -> int:
    """
    Get ROT index

    :param char: initial char
    :param key: rotational cipher index
    :return: cipher index
    """
    id: int = LOWERCASE.index(char.lower())
    if id + key >= len(LOWERCASE):
        return id + key - len(LOWERCASE)
    else:
        return id + key


def cipher_char(char: str, key: int) -> str:
    """
    Cipher char based on ROT index

    :param char: initial char
    :param key: rotational cipher index
    :return: ciphered char
    """
    id: int = get_id(char, key)
    if char.isupper():
        new_char = UPPERCASE[id]
    else:
        new_char = LOWERCASE[id]
    return new_char
