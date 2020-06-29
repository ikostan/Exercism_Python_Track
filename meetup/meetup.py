import calendar
import datetime

WEEKDAYS = ('Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday')

DESCRIPTOR = {'1st': 1,
              '2nd': 2,
              '3rd': 3,
              '4th': 4,
              '5th': 5,
              'last': -1,
              'teenth': 13}


def meetup(year, month, week, day_of_week):

    message = 'Invalid date: ' \
              'year {}, ' \
              'month {}, ' \
              'week {}, ' \
              'day_of_week {}'.format(year,
                                      month,
                                      week,
                                      day_of_week)

    weekdays = list()

    # determine the number of days for a given month
    days = calendar.monthrange(year, month)

    for d in range(1, days[-1] + 1):

        today = datetime.datetime(year, month, d)
        weekday = WEEKDAYS[today.weekday()]

        if weekday == day_of_week:
            weekdays.append(weekday)

        if weekday == day_of_week and week != 'teenth' and len(weekdays) == DESCRIPTOR[week]:
            return datetime.date(year, month, d)

        if weekday == day_of_week and week == 'teenth' and d >= DESCRIPTOR['teenth']:
            return datetime.date(year, month, d)

            # last weekday of the month
        if week == 'last' and weekday == day_of_week and d > days[-1] - 7:
            return datetime.date(year, month, d)

    raise MeetupDayException(message)


class MeetupDayException(Exception):
    pass
