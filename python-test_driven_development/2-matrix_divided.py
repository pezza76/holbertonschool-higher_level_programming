#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    length = len(matrix[0])
    new_matrix = [row[:] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
    for i in range(len(matrix)):
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
