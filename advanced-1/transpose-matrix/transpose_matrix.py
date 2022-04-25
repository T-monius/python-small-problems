'''A module for transposing matrices'''

def transpose(matrix):
    '''Transpose a matrix represented by nested Lists'''
    new_matrix = []
    sample_row = matrix[0]
    for column in range(0, len(sample_row)):
        new_row = []
        for row in matrix:
            element = row[column]
            new_row.append(element)

        new_matrix.append(new_row)

    return new_matrix
