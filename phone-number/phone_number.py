class PhoneNumber(object):

    def __init__(self, phone_number):
        digits_only = ''.join(n for n in phone_number if n.isdigit())

        if not country_code(digits_only):
            raise ValueError('Invalid country code')
        elif not npa(digits_only):
            raise ValueError('Invalid NPA')
        elif not exchange_code(digits_only):
            raise ValueError('Invalid exchange code')

        self.number = digits_only if len(digits_only) == 10 else digits_only[1:]
        self.area_code = npa(digits_only)

    # return formatted phone number:
    def pretty(self):
        if len(self.number) == 10:
            return '({0})-{1}-{2}'.format(self.number[0:3],
                                          self.number[3:6],
                                          self.number[6:])
        else:
            return '({0})-{1}-{2}'.format(self.number[1:3],
                                          self.number[4:7],
                                          self.number[7:])


# Country code validation:
def country_code(digits_only: str):
    if len(digits_only) == 10:
        return True
    elif digits_only[0] == '1' and len(digits_only[1:]) == 10:
        return True
    else:
        return False


# NPA validation:
def npa(digits_only: str):
    npa = [200, 999]

    if npa[0] <= int(digits_only[0:3]) <= npa[1] \
            and len(digits_only) == 10:
        return digits_only[0:3]
    elif npa[0] <= int(digits_only[1:4]) <= npa[1] \
            and len(digits_only) == 11:
        return digits_only[1:4]
    else:
        return False


# Exchange code validation:
def exchange_code(digits_only: str):
    if int(digits_only[3]) > 1 \
            and len(digits_only) == 10:
        return True
    elif int(digits_only[4]) > 1 \
            and len(digits_only) == 11:
        return True
    else:
        return False
