"""
# 367
Easy
Valid Perfect Square

https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:

1 <= num <= 2^31 - 1
"""


def is_perfect_square(num: int) -> bool:
    """
    Solved using binary search
    """

    if num == 1:
        return True

    left = 1
    right = num

    while right - left > 1:
        mid = (left + right) // 2

        u = mid * mid

        if u == num:
            return True
        elif u < num:
            left = mid
        else:
            right = mid

    return False


if __name__ == "__main__":
    assert is_perfect_square(16)
    assert not is_perfect_square(14)
    assert is_perfect_square(100)
