def encode(message: str, rails: int) -> str:
    """
    In the Rail Fence cipher, the message is written
    downwards on successive "rails" of an imaginary
    fence, then moving up when we get to the bottom
    (like a zig-zag). Finally the message is then
    read off in rows.

    :param message:
    :param rails:
    :return:
    """
    return ''.join([''.join(e) for e in get_rails(message, rails)])


def get_rails(message: str, rails: int) -> list:
    encoded: list = [([''] * len(message.replace(' ', ''))) for r in range(rails)]
    row, col, down = 0, 0, True

    for char in message.replace(' ', ''):
        encoded[row][col] = char

        if row == rails - 1 and down:
            down = False

        if row == 0 and not down:
            down = True

        if row < rails and down:
            row += 1

        if row > 0 and not down:
            row -= 1

        col += 1

    return encoded


def decode(encoded_message: str, rails: int) -> str:
    """
    To decrypt a message you take the zig-zag shape
    and fill the ciphertext along the rows.

    :param encoded_message:
    :param rails:
    :return:
    """
    message: str = ''
    decoded: list = get_rails(encoded_message, rails)

    i = 0
    for r, row_decoded in enumerate(decoded):
        for c, col_decoded in enumerate(row_decoded):
            if col_decoded:
                decoded[r][c] = encoded_message[i]
                i += 1

    for c in range(len(decoded[0])):
        for r in range(len(decoded)):
            if decoded[r][c]:
                message += decoded[r][c]

    return message
