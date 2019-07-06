import datetime


def add(moment: datetime):
    '''
    Calculate the moment when someone has lived for 10^9 seconds.
    A gigasecond is 10^9 (1,000,000,000) seconds.
    :param moment:
    :return:
    '''

    # Calculate how many days in one gigasecond
    days = (((10 ** 9) / 60) / 60) / 24

    # A duration expressing the difference between two date, time,
    # or datetime instances to microsecond resolution.
    delta = datetime.timedelta(days)
    return moment + delta
