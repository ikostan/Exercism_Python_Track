def recite(start: int, take=1) -> list:
    """
    Recite the lyrics to that beloved classic, that
    field-trip favorite: 99 Bottles of Beer on the Wall.

    :param start:
    :param take:
    :return:
    """

    lines: list = list()

    for i in range(take):

        if start > 0:

            lines.append(
                '{0} of beer on the wall, {0} of beer.'.format(
                    '{} bottles'.format(start) if start > 1
                    else ('{} bottle'.format(start) if start == 1
                          else 'no more bottles'))
            )

            start -= 1

            lines.append(
                'Take {} down and pass it around, {} of beer on the wall.'.format(
                    'one' if start > 0 else 'it',
                    "{} bottles".format(start) if start > 1
                    else ('{} bottle'.format(start) if start == 1
                          else "no more bottles"))
            )

            if i < take - 1:
                lines.append('')
        else:
            lines.append(
                "No more bottles of beer on the wall, no more bottles of beer."
            )
            lines.append(
                "Go to the store and buy some more, 99 bottles of beer on the wall."
            )

    return lines
