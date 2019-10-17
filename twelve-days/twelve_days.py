# Output the lyrics to 'The Twelve Days of Christmas'
DAYS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

PRESENTS = ["two Turtle Doves, ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "]


def recite(start_verse, end_verse):
    """
    Returns part of 'The Twelve Days of Christmas' verse
    based on function input
    :param start_verse:
    :param end_verse:
    :return:
    """

    presents = []

    for n in range(0, end_verse):
        tmp_str = ''

        if n == 0:
            presents.append("On the {} day of Christmas my true love gave to me: "
                            "{}".format(DAYS[n + 1],
                                        'a Partridge in a Pear Tree.'))
        else:
            for i in range(n, 0, -1):
                tmp_str += PRESENTS[i - 1]

            string = "On the {} day of Christmas my true love gave to me: " \
                     "{}and a Partridge in a Pear Tree.".format(DAYS[n + 1],
                                                                tmp_str)
            presents.append(string)

    return presents[start_verse - 1:]
