def total(basket: list) -> float:
    """
    Calculates the price of any conceivable shopping basket
    (containing only books of the same series), giving as
    big a discount as possible.
    :param basket:
    :return:
    """

    # empty basket
    if not basket:
        return 0

    book_price = 8.0
    total_prices = 0
    discount_combinations = regroup(discount_combinations_generator(basket))

    for combination in discount_combinations:
        total_books = len(combination)
        total_prices += book_price * calculate_discount(total_books) * total_books

    # calculate total price
    return round(total_prices * 100, 0)


def regroup(discount_combinations: list) -> list:
    """
    Regroup unique combinations in order to get total cheapest price
    :param discount_combinations: unique combinations of books
    :return:
    """

    total_books = 0
    for combination in discount_combinations:
        total_books += len(combination)

    min_len = len(discount_combinations[-1])
    i = 0
    if total_books % min_len != 0:
        for x, combination in enumerate(discount_combinations):
            if len(combination) == min_len:
                for b in discount_combinations[i]:
                    if b not in combination:
                        discount_combinations[x].add(b)
                        discount_combinations[i].remove(b)
                        i += 1
                        break

    return discount_combinations


def discount_combinations_generator(basket: list) -> list:
    """
    Generates possible unique groups of books
    :param basket: all books from customer's basket
    :return:
    """
    combinations = list()
    while basket:
        temp = set(basket)
        combinations.append(temp)
        for t in temp:
            basket.remove(t)
    return combinations


def calculate_discount(n: int) -> float:
    """
    If you buy two different books, you get a 5% discount on those two books.
    If you buy 3 different books, you get a 10% discount.
    If you buy 4 different books, you get a 20% discount.
    If you buy all 5, you get a 25% discount.

    :param n: number of books
    :return:
    """

    # One copy of any of the five books -> no discount
    discount = 1.0

    # If you buy two different books, you get a 5% discount
    if n == 2:
        discount = 0.95
    # If you buy 3 different books, you get a 10% discount
    elif n == 3:
        discount = 0.9
    # If you buy 4 different books, you get a 20% discount
    elif n == 4:
        discount = 0.8
    # If you buy all 5, you get a 25% discount.
    elif n == 5:
        discount = 0.75

    return discount
