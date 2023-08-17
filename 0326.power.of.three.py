"""
# 326
Easy
Power of Three

https://leetcode.com/problems/power-of-three/

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


def is_power_of_three(n: int) -> bool:
    if n <= 2 and n != 1:
        return False

    while n > 1:
        if n % 3:
            return False

        n /= 3

    return True


def is_power_of_three(n: int) -> bool:
    while n > 1 and n % 3 == 0:
        n //= 3

    return n == 1


if __name__ == "__main__":
    assert is_power_of_three(27)
    assert not is_power_of_three(0)
    assert not is_power_of_three(-1)
