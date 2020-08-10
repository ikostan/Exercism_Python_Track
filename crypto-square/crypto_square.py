import math


def get_col_row(length: int) -> tuple:
    """
    The size of the rectangle (r x c) should be decided
    by the length of the message, such that c >= r and
    c - r <= 1, where c is the number of columns and r
    is the number of rows.
    :param length:
    :return:
    """
    r = int(math.sqrt(length))
    c = int(math.ceil(math.sqrt(length)))

    if r * c < length:
        r += 1

    return c, r


def get_normalized(row: int, col: int, plain_text_no_empty_chars: str) -> list:
    """
    The plaintext should be organized in to a rectangle.
    Normalized text is x characters long, dictating a rectangle with c * r

    :param row:
    :param col:
    :param plain_text_no_empty_chars:
    :return:
    """
    normalized: list = list()

    start = 0
    end = col
    for r in range(row):
        normalized.append(plain_text_no_empty_chars[start: end])
        start, end = end, (end + col)

    if len(normalized[-1]) < col:
        normalized[-1] = '{}{}'.format(normalized[-1], ' ' * (col - len(normalized[-1])))

    return normalized


def encoded(normalized: list) -> str:
    """
    The coded message is obtained by reading down the columns going left to right.

    :param normalized:
    :return:
    """
    str_encoded: list = list()
    for col in range(len(normalized[0])):
        str_row: str = ''
        for row in range(len(normalized)):
            str_row += normalized[row][col]

        str_encoded.append(str_row)

    return ' '.join(str_encoded)


def cipher_text(plain_text: str) -> str:
    # The input is normalized: the spaces and punctuation are removed
    # from the English text and the message is down-cased.
    plain_text_no_empty_chars: str = ''.join([char.lower() for char in plain_text
                                              if (char.isalpha() or char.isdigit())])
    
    if not plain_text_no_empty_chars:
        return ''

    col, row = get_col_row(len(plain_text_no_empty_chars))

    # The plaintext should be organized in to a rectangle.
    normalized: list = get_normalized(row, col, plain_text_no_empty_chars)

    # Encoded text
    return encoded(normalized)
