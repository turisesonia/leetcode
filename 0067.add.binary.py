"""
# 67
Easy
Add Binary

https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def add_binary(a: str, b: str) -> str:
    ml = -1 * max(len(a), len(b))
    carry = 0
    i = -1
    r = ""

    while i >= ml:
        an = int(a[i]) if abs(i) <= len(a) else 0
        bn = int(b[i]) if abs(i) <= len(b) else 0

        u = an + bn + carry

        if u > 1:
            u -= 2
            carry = 1
        else:
            carry = 0

        r = str(u) + r
        i -= 1

    if carry:
        r = "1" + r

    return r


if __name__ == "__main__":
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
