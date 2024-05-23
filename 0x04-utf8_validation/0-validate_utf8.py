#!/usr/bin/env python3
"""method that determines if a given
data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    remaining_bytes = 0

    mask1 = 0b10000000  # 1 << 7
    mask2 = 0b01000000  # 1 << 6

    for byte in data:
        if remaining_bytes == 0:
            leading_ones = count_leading_ones(byte)
            if leading_ones == 0:
                continue

            if leading_ones == 1 or leading_ones > 4:
                return False

            remaining_bytes = leading_ones - 1
        else:
            if not is_valid_continuation_byte(byte, mask1, mask2):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0


def count_leading_ones(byte):
    """Counts the number of leading 1 bits in a byte."""
    mask = 0b10000000  # 1 << 7
    count = 0
    while byte & mask:
        count += 1
        mask >>= 1
    return count


def is_valid_continuation_byte(byte, mask1, mask2):
    """Checks if a byte is a valid UTF-8 continuation byte."""
    return byte & mask1 and not (byte & mask2)
