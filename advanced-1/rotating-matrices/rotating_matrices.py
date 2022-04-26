'''A module for rotating matrices represented by lists of lists'''

def rotate90(matrix):
    '''Return a new matrix that is the rotated version of input matrix
       without mutating'''
    column_total = len(matrix[0])
    rotated_matrix = []

    for column in range(0, column_total):
        new_row = [row[column] for row in reversed(matrix)]
        rotated_matrix.append(new_row)

    return rotated_matrix
