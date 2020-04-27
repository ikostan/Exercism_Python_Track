"""
The mission is to write a piece of code to calculate the price
of any conceivable shopping basket (containing only books of the
same series), giving as big a discount as possible.
"""

BOOK_PRICE = 8.0


TOTAL_PRICE_AFTER_DISCOUNT = {
    1: 1.0 * BOOK_PRICE * 1,
    2: 0.95 * BOOK_PRICE * 2,
    3: 0.9 * BOOK_PRICE * 3,
    4: 0.8 * BOOK_PRICE * 4,
    5: 0.75 * BOOK_PRICE * 5,
}


def total(basket: list) -> float:
    """
    Calculates the price of any conceivable shopping basket
    (containing only books of the same series), giving as
    big a discount as possible.

    :param basket: list of books
    :return: big discount as possible
    """
    # empty basket
    if not basket:
        return 0

    discount_combinations = regroup(unique_combinations(basket))

    total_prices = sum(TOTAL_PRICE_AFTER_DISCOUNT[len(combination)]
                       for combination in discount_combinations)

    return round(total_prices * 100, 0)


def regroup(discount_combinations: list) -> list:
    """
    Regroup unique combinations in order to get total cheapest price

    :param discount_combinations: unique combinations of books
    :return: unique combinations of books based on biggest discount
    """
    total_books = sum(len(combination)
                      for combination in discount_combinations)

    i, min_len = 0, len(discount_combinations[-1])

    # In some cases there is a big gap between the biggest vs smallest combination.
    # Because of that, the total discount may be less than max possible.
    # In order to solve the problem, combinations must be reshuffled.
    if total_books % min_len != 0:
        for combination_index, combination in enumerate(discount_combinations):
            # In case we found smallest combination do following:
            # 1. Take the biggest one (use index, starts from 0).
            # 2. Find the book that not in smallest and move it there.
            # 3. Remove the same book from the biggest combination.
            # 4. Update index of the biggest combination.
            if len(combination) == min_len:
                for book in discount_combinations[i]:
                    if book not in combination:
                        discount_combinations[combination_index].add(book)
                        discount_combinations[i].remove(book)
                        i += 1
                        break
    return discount_combinations


def unique_combinations(basket: list) -> list:
    """
    Returns possible unique groups of books

    :param basket: all books from customer's basket
    :return: unique combinations of books
    """
    combinations = list()
    basket = basket[:]

    while basket:
        temp = set(basket)
        combinations.append(temp)
        for t in temp:
            basket.remove(t)

    return combinations
