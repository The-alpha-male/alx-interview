#!/usr/bin/env python3
"""Rotate 2D Matrix by 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix by 90 degrees clockwise"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
