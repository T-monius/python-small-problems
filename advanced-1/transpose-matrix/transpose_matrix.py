'''A module for transposing matrices'''

def transpose(matrix):
    '''Transpose a matrix represented by nested Lists'''
    new_matrix = []
    for idx in range(0, len(matrix)):
        new_row = []
        for row in matrix:
            element = row[idx]
            new_row.append(element)

        new_matrix.append(new_row)

    return new_matrix
