#!/usr/bin/python3
"""Rotate 2D Matrix."""


def rotate_2d_matrix(matrix):
    """2D matrix, rotate it 90 degrees clockwise and Returns: Nothing.
    """
    n = len(matrix)


    # Transpose of the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    # Reverse the row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
