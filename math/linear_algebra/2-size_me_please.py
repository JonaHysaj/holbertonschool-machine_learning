#!/usr/bin/env python3
def matrix_shape(matrix):
    matrix_shape = __import__('2-size_me_please').matrix_shape
    result = []
    while (type(matrix) is list):
        result.append(len(matrix))
        matrix = matrix[0]
        return result
    mat1 = [[1, 2], [3, 4]]
    print(matrix_shape(mat1))
    mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
            print(matrix_shape(mat2))
