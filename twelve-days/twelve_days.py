# Output the lyrics to 'The Twelve Days of Christmas'
DAYS = ["first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"]

PRESENTS = ["a Partridge in a Pear Tree.",
            "two Turtle Doves",
            "three French Hens",
            "four Calling Birds",
            "five Gold Rings",
            "six Geese-a-Laying",
            "seven Swans-a-Swimming",
            "eight Maids-a-Milking",
            "nine Ladies Dancing",
            "ten Lords-a-Leaping",
            "eleven Pipers Piping",
            "twelve Drummers Drumming"]


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
                            "{}".format(DAYS[n], PRESENTS[0]))
        else:
            for i in range(n, 0, -1):
                tmp_str = '{}{}{}'.format(tmp_str, PRESENTS[i], ', ')

            string = "On the {} day of Christmas my true love gave to me: " \
                     "{}and {}".format(DAYS[n], tmp_str, PRESENTS[0])
            presents.append(string)

    return presents[start_verse - 1:]
