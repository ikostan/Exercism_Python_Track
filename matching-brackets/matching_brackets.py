def is_paired(input_string: str) -> bool:

    input_string = clean_input_string(input_string)

    if len(input_string) % 2 != 0:
        return False

    while input_string:
        if not remove_bracket(input_string[0], input_string):
            return False

    return True


def remove_bracket(bracket: str, input_string: list) -> bool:

    pairs = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    if bracket not in pairs:
        return False

    if input_string[1] == pairs[bracket]:
        del input_string[1]
        del input_string[0]
        return True
    elif input_string[-1] == pairs[bracket]:
        del input_string[-1]
        del input_string[0]
        return True


def clean_input_string(input_string: str) -> list:
    template = '[]{}()'
    return [char for char in input_string if char in template]