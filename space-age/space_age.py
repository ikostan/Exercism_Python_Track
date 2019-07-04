class SpaceAge(object):
    # Earth: orbital period 365.25 Earth days, or 31557600 seconds
    days_in_earth_year = 365.25
    seconds_in_earth_year = 31557600
    seconds_in_earth_day = seconds_in_earth_year / days_in_earth_year

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        '''
        Mercury: orbital period 0.2408467 Earth years
        :return:
        '''

        orbital_period = 0.2408467
        return self._calc_age(orbital_period)

    def on_venus(self):
        '''
        Venus: orbital period 0.61519726 Earth years
        :return:
        '''

        orbital_period = 0.61519726
        return self._calc_age(orbital_period)

    def on_earth(self):
        '''
        Earth: orbital period 365.25 Earth days, or 31557600 seconds
        :return:
        '''

        orbital_period = 1
        return self._calc_age(orbital_period)

    def on_mars(self):
        '''
        Mars: orbital period 1.8808158 Earth years
        :return:
        '''

        orbital_period = 1.8808158
        return self._calc_age(orbital_period)

    def on_jupiter(self):
        '''
        Jupiter: orbital period 11.862615 Earth years
        :return:
        '''

        orbital_period = 11.862615
        return self._calc_age(orbital_period)

    def on_saturn(self):
        '''
        Saturn: orbital period 29.447498 Earth years
        :return:
        '''

        orbital_period = 29.447498
        return self._calc_age(orbital_period)

    def on_uranus(self):
        '''
        Uranus: orbital period 84.016846 Earth years
        :return:
        '''

        orbital_period = 84.016846
        return self._calc_age(orbital_period)

    def on_neptune(self):
        '''
        Neptune: orbital period 164.79132 Earth years
        :return:
        '''

        orbital_period = 164.79132
        return self._calc_age(orbital_period)

    def _calc_age(self, orbital_period):
        return round(
            (
                    (self.seconds / self.seconds_in_earth_day) /
                    self.days_in_earth_year) /
            orbital_period, 2)
