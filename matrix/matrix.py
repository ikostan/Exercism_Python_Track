class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(number) for number in m.split(' ')] for m in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [m[index - 1] for m in self.matrix]

