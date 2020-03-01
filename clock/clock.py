class Clock:
    """
    A clock that handles times without dates.
    """

    DAY_AND_NIGHT = 24
    HOUR = 60

    def __init__(self, hour: int, minute: int):
        """
        Constructor for the Clock class.
        Set hours and minutes by 24 hour clock.
        :param hour:
        :param minute:
        """
        total_minutes = (hour * self.HOUR) + minute
        self.__hours = self.__calc_hours(total_minutes)
        self.__minutes = self.__calc_minutes(total_minutes)

    def __calc_minutes(self, total_minutes: int) -> int:
        """
        Calculate minutes when update occurs
        :param total_minutes:
        :return:
        """
        return total_minutes % self.HOUR

    def __calc_hours(self, total_minutes: int) -> int:
        """
        Calculate hours when update occurs
        :param total_minutes:
        :return:
        """
        return (total_minutes // self.HOUR) % self.DAY_AND_NIGHT

    def __repr__(self):
        """
        Convert to string
        :return:
        """
        return "{:02d}:{:02d}".format(self.__hours, self.__minutes)

    def __eq__(self, other) -> bool:
        """
        Compare between objects.
        Two clocks that represent the same time
        should be equal to each other.
        :param other:
        :return:
        """
        return self.__class__ == other.__class__ and \
               self.__hours == other.__hours and \
               self.__minutes == other.__minutes

    def __add__(self, minutes: int):
        """
        Add minutes and update Clock.
        The Clock should be able to add
        minutes to it.
        :param minutes:
        :return:
        """
        total_minutes = (self.__hours * self.HOUR + self.__minutes) + minutes
        return Clock(self.__calc_hours(total_minutes),
                     self.__calc_minutes(total_minutes))

    def __sub__(self, minutes: int):
        """
        Subtract minutes and update Clock.
        The Clock should be able to subtract
        minutes to it.
        :param minutes:
        :return:
        """

        total_minutes = (self.__hours * self.HOUR + self.__minutes) - minutes
        return Clock(self.__calc_hours(total_minutes),
                     self.__calc_minutes(total_minutes))
