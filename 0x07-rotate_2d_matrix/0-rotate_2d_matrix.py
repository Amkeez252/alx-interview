#!/usr/bin/python3
"""Rotate 2D Matrix."""


def rotate_2d_matrix(matrix):
    net = len(matrix)

    for i in range(net):
        for j in range(i, net):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    # Reverse the row    
    for i in range(net):
        matrix[i] = matrix[i][::-1]
