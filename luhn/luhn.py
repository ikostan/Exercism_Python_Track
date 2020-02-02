class Luhn:
    """
    Given a number determine whether or not
    it is valid per the Luhn formula.
    """

    def __init__(self, card_num: str):

        self.card_num = card_num

        if self.__is_valid_input():
            self.__card_num = \
                [int(char) for char in
                 self.card_num if char.isdigit()]
            self.__digits_processor()

    # Declaring private method
    def __digits_processor(self):
        """
        The first step of the Luhn algorithm is to double
        every second digit, starting from the right.
        If doubling the number results in a number greater
        than 9 then subtract 9 from the product.
        :return:
        """

        self.__card_num.reverse()

        for i, n in enumerate(self.__card_num):
            if i % 2 != 0:
                self.__card_num[i] = n * 2
                if self.__card_num[i] > 9:
                    self.__card_num[i] = self.__card_num[i] - 9

        self.__card_num.reverse()

    # Declaring private method
    def __is_valid_input(self) -> bool:
        """
        Test if there any garbage
        (non digit chars) in user input
        :return:
        """
        self.card_num = self.card_num.replace(' ', '')

        for char in self.card_num:
            if not char.isdigit():
                return False

        return True

    def valid(self) -> bool:
        """
        Sum all of the digits.
        If the sum is evenly divisible by 10,
        then the number is valid.
        :return:
        """

        if not self.__is_valid_input():
            return False

        if len(self.__card_num) < 2:
            return False

        return sum(self.__card_num) % 10 == 0
