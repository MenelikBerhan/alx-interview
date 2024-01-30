#!/usr/bin/python3
"""
UTF-8 Validation function
"""
from re import match


def validUTF8(data: 'list[int]') -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: a list of integers where each integer represents 1 byte of data.
            A character in UTF-8 can be 1 to 4 bytes long and `data` can
            contain multiple characters. Only the 8 least significant bits of
            each integer is used.

    Returns:
        bool: True if `data` is a valid UTF-8 encoding, else returns False.
    """
    # if data doesn't contain list of integers return False
    if not data or not all([type(n) == int and n >= 0 for n in data]):
        return False

    # convert each no. in data to a binary of 8 bits
    binary = []                     # list of 8 bit binary numbers string
    for n in data:
        n = -n if n < 0 else n      # to avoid '-' in binary representation
        # get the 8 least significant bits and remove leading '0b' prefix,
        # and add leading zeros if needed
        b = bin(n & 0xff)[2:].zfill(8)
        binary.append(b)

    # valid utf-8 encoding patterns for 1 - 4 byte caharacters
    utf_1_byte = r'^0[0,1]{7}$'
    utf_2_byte = r'^110([0,1]{5})10([0,1]{6})$'
    utf_3_byte = r'^1110([0,1]{4})10([0,1]{6})10([0,1]{6})$'
    utf_4_byte = r'^11110([0,1]{3})10([0,1]{6})10([0,1]{6})10([0,1]{6})$'

    i = 0
    len_data = len(data)
    # for each check if they match utf-8 encoding (from 1 to 4 bytes)
    while i < len_data:
        if match(utf_1_byte, binary[i]):
            i += 1

        elif i + 1 < len_data and match(utf_2_byte, "".join(binary[i: i + 2])):
            utf = match(utf_2_byte, "".join(binary[i: i + 2])).groups()
            utf_value = int("".join(utf), 2)
            if utf_value < 0x0080:      # overlong encoding
                return False
            i += 2

        elif i + 2 < len_data and match(utf_3_byte, "".join(binary[i: i + 3])):
            utf = match(utf_3_byte, "".join(binary[i: i + 3])).groups()
            utf_value = int("".join(utf), 2)
            if utf_value < 0x0800:      # overlong encoding
                return False
            i += 3

        elif i + 3 < len_data and match(utf_4_byte, "".join(binary[i: i + 4])):
            utf = match(utf_4_byte, "".join(binary[i: i + 4])).groups()
            utf_value = int("".join(utf), 2)
            if utf_value < 0x10000:     # overlong encoding
                return False
            i += 4

        else:
            return False

    return True
