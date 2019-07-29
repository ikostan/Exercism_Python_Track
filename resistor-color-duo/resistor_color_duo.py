def value(colors: list):
    '''
    Each resistor has a resistance value.
    Manufacturers print color-coded bands onto the resistors to denote their resistance values.
    Each band acts as a digit of a number.
    The program will take two colors as input, and output the correct number.
    :param colors:
    :return:
    '''

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

    result = ''
    for color in colors:
        if color not in encoded_colors.keys():
            raise Exception("Invalid color: {}".format(color))
        result += str(encoded_colors[color])

    return int(result)
