"""
# 405
Easy
Convert a Number to Hexadecimal

https://leetcode.com/problems/convert-a-number-to-hexadecimal/

Given an integer num, return a string representing its hexadecimal representation.
For negative integers, two's complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"

Constraints:
-2^31 <= num <= 2^31 - 1
"""


def to_hex(num: int) -> str:
    if num == 0:
        return "0"

    alph = "0123456789abcdef"

    if num < 0:
        num = 2**32 + num

    result = ""

    while num > 0:
        result = alph[num % 16] + result

        num //= 16

    return result


if __name__ == "__main__":
    assert to_hex(26) == "1a"
    assert to_hex(-1) == "ffffffff"
