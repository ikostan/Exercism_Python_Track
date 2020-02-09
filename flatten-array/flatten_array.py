def flatten(iterable: list) -> list:
    """
    A function that accepts an arbitrarily-deep
    nested list-like structure and returns a
    flattened structure without any nil/null values.

    For Example:
        input: [1,[2,3,null,4],[null],5]
        output: [1,2,3,4,5]

    :param iterable:
    :return:
    """
    result = list()
    get_all_digits(iterable, result)
    return result


def get_all_digits(iterable, result: list):

    if isinstance(iterable, int):
        result.append(iterable)

    if isinstance(iterable, list):
        for item in iterable:
            get_all_digits(item, result)
