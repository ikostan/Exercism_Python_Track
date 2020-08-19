HANDSHAKE = {
    1: 'wink',
    10: 'double blink',
    100: 'close your eyes',
    1000: 'jump',
    10000: 'reverse'
}


def decimal_to_binary(n: int):
    """
    Function to convert Decimal number to Binary number 
    
    :param n: 
    :return: 
    """
    return int("{0:b}".format(n))


def get_key(val):
    """
    Get dict key by value

    :param val:
    :return:
    """
    for key, value in HANDSHAKE.items():
        if val == value:
            return key


def sort_results(results: list, reverse: bool) -> list:
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, val in enumerate(results):
            if i + 1 < len(results):
                if not reverse:
                    if get_key(results[i]) > get_key(results[i + 1]):
                        results[i], results[i + 1] = results[i + 1], results[i]
                        is_sorted = False
                else:
                    if get_key(results[i]) < get_key(results[i + 1]):
                        results[i], results[i + 1] = results[i + 1], results[i]
                        is_sorted = False
    return results


def commands(number: int) -> list:
    """
    Given a decimal number, convert it to the appropriate 
    sequence of events for a secret handshake.
    
    :param number: a decimal number,
    :return: sequence of events for a secret handshake
    """
    results: list = list()
    n: int = decimal_to_binary(number)
    # 10000 = Reverse the order of the
    # operations in the secret handshake.
    reverse = True if n >= 10000 else False
    for key in sorted(HANDSHAKE.keys(), reverse=True):
        if key <= n:
            if key != 10000:
                results.append(HANDSHAKE[key])
            n -= key

    return sort_results(results, reverse)
