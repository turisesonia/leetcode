"""
# 9
Easy
https://leetcode.com/problems/palindrome-number

Given an integer x, return true if x is a palindrome, and false otherwise.

palindrome => 121, 12321, 1234321
"""


def is_palindrome(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """

    x = str(x)

    for i in range(int(len(x) / 2)):
        if x[i] != x[len(x) - 1 - i]:
            return False

    return True


def is_palindrome(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """

    x = str(x)

    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False

    return True


if __name__ == "__main__":
    assert is_palindrome(121) == True
    assert is_palindrome(1231) == False
    assert is_palindrome(12321) == True
    assert is_palindrome(-12321) == False
