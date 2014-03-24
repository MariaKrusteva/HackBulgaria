def transposed(matrix):
    return [list(column) for column in zip(*matrix)]


def sum_rows(matrix):
    return [sum(x) for x in matrix]


def sum_cols(matrix):
    return sum_rows(transposed(matrix))


def sum_diagonal(matrix):
    return sum([matrix[i][i] for i in range(0, len(matrix))])


def sum_diagonal2(matrix):
    return sum([matrix[-i][-i] for i in range(-len(matrix) + 1, 1)])


def magic_square(matrix):
    if sum_cols(matrix).count(sum_cols(matrix)[0]) != len(matrix):
        return False
    if sum_rows(matrix).count(sum_rows(matrix)[0]) != len(matrix):
        return False
    return sum_cols(matrix)[0] == sum_rows(matrix)[0] == sum_diagonal(matrix) == sum_diagonal2(matrix)
