"""
# 342
Easy
Power of Four

https://leetcode.com/problems/power-of-four/

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


def is_power_of_four(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0


if __name__ == "__main__":
    assert is_power_of_four(1)
    assert is_power_of_four(16)
    assert not is_power_of_four(5)
    assert is_power_of_four(64)
