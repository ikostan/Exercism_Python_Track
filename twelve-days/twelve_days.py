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

PRESENTS = [" twelve Drummers Drumming,",
            " eleven Pipers Piping,",
            " ten Lords-a-Leaping,",
            " nine Ladies Dancing,",
            " eight Maids-a-Milking,",
            " seven Swans-a-Swimming,",
            " six Geese-a-Laying,",
            " five Gold Rings,",
            " four Calling Birds,",
            " three French Hens,",
            " two Turtle Doves,",
            " and a Partridge in a Pear Tree."]


def recite(start_verse, end_verse):
	"""
    Returns part of 'The Twelve Days of Christmas' verse
    based on function input
    :param start_verse:
    :param end_verse:
    :return:
    """

	presents = ''

	if end_verse == 1:
		presents = ' a Partridge in a Pear Tree.'
	else:
		for i in range(len(PRESENTS) - end_verse, len(PRESENTS)):
			presents += PRESENTS[i]

	return ['On the {} day of Christmas my true love gave to me:{}'.format(DAYS[start_verse], presents)]
