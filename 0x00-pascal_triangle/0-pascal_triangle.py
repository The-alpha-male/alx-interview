#!/usr/bin/python3
"""Pascals Triangle Module"""


def pascal_triangle(n):
    """Pascals Triangle"""
    if n == 0:
        return []
    array = []
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(array[i-1][j-1] + array[i-1][j])
        array.append(temp)
    return array
