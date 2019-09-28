def sum_of_multiples(limit, multiples):
    """
    Given a number, find the sum of all the unique multiples
    of particular numbers up to but not including that number.

    If we list all the natural numbers below 20 that are
    multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

    The sum of these multiples is 78.
    :param limit:
    :param multiples:
    :return:
    """

    if not multiples:
        return 0

    results = []

    for i in range(min(multiples), limit):
        for m in multiples:
            try:
                if i % m == 0:
                    results.append(i)
                    break
            except ZeroDivisionError:
                continue

    return sum(results)
