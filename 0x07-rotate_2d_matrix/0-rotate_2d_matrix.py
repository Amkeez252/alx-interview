#!/usr/bin/python3
"""
 Rotate 2D Matrix
 Given an n x n 2D matrix, rotate it 90 degrees clockwise.
 """

def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # Transpose of the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
