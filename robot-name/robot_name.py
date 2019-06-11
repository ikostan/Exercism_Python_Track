class Robot(object):
    def __init__(self):
        self.name = ''
        self.reset()

    def reset(self):
        '''
        Every once in a while we need to reset a robot
        to its factory settings, which means that their
        name gets wiped. The next time you ask,
        it will respond with a new random name.

        The first time you boot them up, a random name is generated in
        the format of two uppercase letters followed by three digits,
        such as RX837 or BC811.
        :return:
        '''
        import string
        import random
        old_name = self.name

        while old_name == self.name:
            self.name = ''
            for n in range(0, 2):
                self.name += string.ascii_uppercase[random.randint(0, 25)]

            for n in range(0, 3):
                self.name += str(random.randint(0, 9))


