#!/usr/bin/python3

"""
Minimum Operations
"""


def minOperations(n):
    """Calculates the minimum operations needed to result
    to an exact number of n H characters in the file.
    Calculates the minimum number of operations needed to transform
    a string of length n into a string of exactly n H characters"""
    if n <= 1:
        return 0
    i = 2
    count = 0
    while i <= n:
        if n % i == 0:
            count += i
            n = n / i
        else:
            i += 1
    return count
