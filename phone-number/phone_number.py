class Phone(object):

    def __init__(self, phone_number):
        digits_only = ''.join(n for n in phone_number if n.isdigit())

        if self._country_code(digits_only):
            if self._npa(digits_only):
                if self._exchange_code(digits_only):
                    self.number = digits_only if len(digits_only) == 10 else digits_only[1:]
                    self.area_code = self._npa(digits_only)
                else:
                    raise ValueError('Invalid exchange code')
            else:
                raise ValueError('Invalid NPA')
        else:
            raise ValueError('Invalid country code')

    # return formatted phone number:
    def pretty(self):
        if len(self.number) == 10:
            return '({0}) {1}-{2}'.format(self.number[0:3],
                                          self.number[3:6],
                                          self.number[6:])
        else:
            return '({0}) {1}-{2}'.format(self.number[1:3],
                                          self.number[4:7],
                                          self.number[7:])

    # Country code validation:
    def _country_code(self, digits_only: str):
        if len(digits_only) == 10:
            return True
        elif digits_only[0] == '1' and len(digits_only[1:]) == 10:
            return True
        else:
            return False

    # NPA validation:
    def _npa(self, digits_only: str):
        npa = [200, 999]

        if npa[0] <= int(digits_only[0:3]) <= npa[1] and len(digits_only) == 10:
            return digits_only[0:3]
        elif npa[0] <= int(digits_only[1:4]) <= npa[1] and len(digits_only) == 11:
            return digits_only[1:4]
        else:
            return False

    # Exchange code validation:
    def _exchange_code(self, digits_only: str):
        if int(digits_only[3]) > 1 and len(digits_only) == 10:
            return True
        elif int(digits_only[4]) > 1 and len(digits_only) == 11:
            return True
        else:
            return False

