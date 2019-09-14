def saddle_points(matrix):
    """
    Detect saddle points in a matrix.
    :param matrix:
    :return:
    """

    # Return empty dict in case matrix is empty
    if len(matrix) == 0:
        return [dict()]

    # Raise ValueError in case one of the list members has a different length
    if len(max(matrix)) != len(min(matrix)):
        raise ValueError(".+")

    answer = []

    for col_i, col in enumerate(matrix[0]):

        # Collect all column members into one list
        column = []
        for row_i, row in enumerate(matrix):
            column.append(matrix[row_i][col_i])

        for i, c in enumerate(column):
            if c > min(column):
                continue
            # It's called a "saddle point" because it is greater than or equal
            # to every element in its row and less than or equal to
            # every element in its column.
            else:
                if max(matrix[i]) == c:
                    answer.append({"row": i + 1, "column": col_i + 1})

    return [dict()] if len(answer) == 0 else answer
