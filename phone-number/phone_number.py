class Phone(object):

    def __init__(self, phone_number):
        print('Raw data: {0}'.format(phone_number))  # debug only

        npa = [200, 999]
        digits_only = ''.join(n for n in phone_number if n.isdigit())
        print('Formatted number: {0}'.format(digits_only))  # debug only

        if len(digits_only) == 10:
            #  print('NPA: {0}'.format(digits_only[0:3]))  # debug only
            #  NPA validation
            if npa[0] <= int(digits_only[0:3]) <= npa[1]:
                print('Exchange code: {0}'.format(digits_only[3]))  # debug only
                # exchange code validation
                if int(digits_only[3]) > 1:
                    self.number = digits_only
                    self.area_code = digits_only[0:3]
                else:
                    ValueError('Invalid exchange code')
            else:
                raise ValueError('Invalid NPA')
        elif digits_only[0] == '1' and len(digits_only[1:]) == 10:
            #  print('NPA: {0}'.format(digits_only[1:4]))  # debug only
            #  NPA validation
            if npa[0] <= int(digits_only[1:4]) <= npa[1]:
                print('Exchange code: {0}'.format(digits_only[4]))  # debug only
                # exchange code validation
                if int(digits_only[4]) > 1:
                    self.number = digits_only[1:]
                    self.area_code = digits_only[1:4]
                else:
                    ValueError('Invalid exchange code')
            else:
                raise ValueError('Invalid NPA')
        else:
            raise ValueError('Invalid phone number')

    def pretty(self):
        if len(self.number) == 10:
            return '({0}) {1}-{2}'.format(self.number[0:3],
                                          self.number[3:6],
                                          self.number[6:])
        else:
            return '({0}) {1}-{2}'.format(self.number[1:3],
                                          self.number[4:7],
                                          self.number[7:])

