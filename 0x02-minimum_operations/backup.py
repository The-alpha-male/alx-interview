#!/usr/bin/env python3
"""Python minimum operations"""


def minOperations(n: int) -> int:
    """Calculates the minimum operations needed to result
    to an exact number of n H characters in the file.
    Calculates the minimum number of operations needed to transform
    a string of length n into a string of exactly n H characters"""

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
