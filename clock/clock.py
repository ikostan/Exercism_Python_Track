class Clock:
    """
    A clock that handles times without dates.

    The Clock should be able to add and subtract
    minutes to it.

    Two clocks that represent the same time
    should be equal to each other.
    """

    DAY_AND_NIGHT = 24
    HOUR = 60

    def __init__(self, hour: int, minute: int):
        """
        Constructor for the Clock class
        Set hours and minutes by 24 hour clock
        :param hour:
        :param minute:
        """

        if hour == 0 or hour == self.DAY_AND_NIGHT:
            self.__hours = self.DAY_AND_NIGHT
        elif hour > 0:
            self.__hours = (hour % self.DAY_AND_NIGHT)
        else:
            self.__hours = abs(hour % self.DAY_AND_NIGHT)

        if 0 <= minute < self.HOUR:
            self.__minutes = minute % self.HOUR
        elif minute > self.HOUR:
            self.__minutes = minute % self.HOUR
            temp_h = (self.__hours + (minute // self.HOUR)) % self.DAY_AND_NIGHT
            self.__hours = temp_h if temp_h != 0 else self.DAY_AND_NIGHT
        else:
            self.__minutes = abs(minute % self.HOUR)
            self.__hours = abs((self.__hours + (minute // self.HOUR)) % self.DAY_AND_NIGHT)

    def __repr__(self):
        """
        Convert to string
        :return:
        """
        return "{:02d}:{:02d}".format(self.__hours if self.__hours < self.DAY_AND_NIGHT else 0,
                                      self.__minutes)

    def __eq__(self, other) -> bool:
        """
        Compare between objects
        :param other:
        :return:
        """
        return self.__class__ == other.__class__ and \
               self.__hours == other.__hours and \
               self.__minutes == other.__minutes

    def __add__(self, minutes: int):
        """
        Add minutes and update Clock
        :param minutes:
        :return:
        """
        total_minutes = self.__minutes + minutes
        total_hours = total_minutes // self.HOUR + self.__hours

        hours = total_hours % self.DAY_AND_NIGHT
        minutes = total_minutes % self.HOUR

        return Clock(hours, minutes)

    def __sub__(self, minutes: int):
        """
        Subtract minutes and update Clock
        :param minutes:
        :return:
        """
        hours = self.__hours - (minutes // self.HOUR)
        minutes = self.__minutes - (minutes % self.HOUR)

        return Clock(hours, minutes)
