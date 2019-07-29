encoded_colors = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }


def color_code(color):
    '''
    Resistors have color coded bands, where each color maps to a number.
    The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number.
    :param color:
    :return:
    '''
    return encoded_colors[color]


def colors():
    '''
    Mnemonics map the colors to the numbers, that, when stored as an array,
    happen to map to their index in the array:
    Better Be Right Or Your Great Big Values Go Wrong.
    ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white',]
    :return:
    '''
    result = []
    indexes = sorted(list(encoded_colors.values()))

    for i in indexes:
        for key, value in encoded_colors.items():
            if value == i:
                result.append(key)
                break

    return result
