class Luhn:
    """
    Given a number determine whether or not
    it is valid per the Luhn formula.
    """

    def __init__(self, card_num: str):

        self.card_num = card_num.replace(' ', '')

        self.__card_num_list = \
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
        for i in range(len(self.__card_num_list) - 2, -1, -2):
            self.__card_num_list[i] = self.__card_num_list[i] * 2
            if self.__card_num_list[i] > 9:
                self.__card_num_list[i] = self.__card_num_list[i] - 9

    def valid(self) -> bool:
        """
        Sum all of the digits.
        If the sum is evenly divisible by 10,
        then the number is valid.
        :return:
        """

        for char in self.card_num:
            if not char.isdigit():
                return False

        if len(self.card_num) < 2:
            return False

        return sum(self.__card_num_list) % 10 == 0
