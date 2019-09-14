def score(x, y):
    """
    Returns the earned points in a single toss of a Darts game

    :param x:
    :param y:
    :return:
    """

    radius = 10  # The outer circle has a radius of 10 units.
    landing_point = (x - 0)**2 + (y - 0)**2

    # If the dart lands outside the target, player earns no points (0 points).
    if landing_point > radius ** 2:
        points = 0

    # If the dart lands in the outer circle of the target, player earns 1 point.
    # The middle circle a radius of 5 units.
    if (radius / 2) ** 2 < landing_point <= radius ** 2:
        points = 1

    # If the dart lands in the middle circle of the target, player earns 5 points.
    if 1 ** 2 < landing_point <= (radius / 2) ** 2:
        points = 5

    # If the dart lands in the inner circle of the target, player earns 10 points.
    # The inner circle a radius of 1
    if landing_point <= 1 ** 2:
        points = 10

    return points
