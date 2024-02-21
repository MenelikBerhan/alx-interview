#!/usr/bin/python3
"""Rotate 2D Matrix Inplace
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """Rotates an `n x n` matrix 90 degrees clockwise and inplace,
    by first transposing the matrix, then reversing each row."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # transpose matrix
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse order in row
        matrix[i].reverse()
