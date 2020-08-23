class Queen:
    """
    Given the position of two queens on a chess board,
    indicate whether or not they are positioned so that
    they can attack each other.
    """

    def __init__(self, row, column):
        # A chessboard can be represented by an 8 by 8 array.
        if row < 0 or column < 0 or row > 7 or column > 7:
            raise ValueError("Queen must have row on board!")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """
        In the game of chess, a queen can attack pieces
        which are on the same row, column, or diagonal.
        
        :param another_queen:
        :return:
        """

        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError('Test queens same position can attack!')

        if self.row == another_queen.row:
            return True

        if self.column == another_queen.column:
            return True

        if max(self.row, another_queen.row) - min(self.row, another_queen.row) == \
                max(self.column, another_queen.column) - min(self.column, another_queen.column):
            return True

        return False
