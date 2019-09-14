class Matrix:
    def __init__(self, matrix_string):
        """
        convert input string into 2D matrix,
        including parsing sub strings to integers
        :param matrix_string:
        """
        self.matrix = [[int(number) for number in m.split(' ')]
                       for m in matrix_string.split('\n')]

    def row(self, index):
        """
        returns row by index
        :param index:
        :return:
        """
        return self.matrix[index - 1]

    def column(self, index):
        """
        returns column by index
        :param index:
        :return:
        """
        return [m[index - 1] for m in self.matrix]

