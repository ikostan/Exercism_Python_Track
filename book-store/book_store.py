"""
The mission is to write a piece of code to calculate the price
of any conceivable shopping basket (containing only books of the
same series), giving as big a discount as possible.
"""


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

    discount_combinations = regroup(unique_combinations(basket))

    total_prices = sum(calculate_total(combination)
                       for combination in discount_combinations)

    return round(total_prices * 100, 0)


def regroup(discount_combinations: list) -> list:
    """
    Regroup unique combinations in order to get total cheapest price
    :param discount_combinations: unique combinations of books
    :return:
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
    :return:
    """
    combinations = list()
    while basket:
        temp = set(basket)
        combinations.append(temp)
        for t in temp:
            basket.remove(t)

    return combinations


def calculate_total(combination: list) -> float:
    """
    If you buy two different books, you get a 5% discount on those two books.
    If you buy 3 different books, you get a 10% discount.
    If you buy 4 different books, you get a 20% discount.
    If you buy all 5, you get a 25% discount.

    :param combination: combination of books
    :return: total price
    """
    book_price = 8.0
    amount = len(combination)
    return DISCOUNT[amount] * book_price * amount


DISCOUNT = {
    1: 1.0,
    2: 0.95,
    3: 0.9,
    4: 0.8,
    5: 0.75
}
