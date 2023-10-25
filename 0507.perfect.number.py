"""
# 507
Easy
Perfect Number

https://leetcode.com/problems/perfect-number/

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false

Constraints:

1 <= num <= 108
"""


def check_perfect_number(num: int) -> bool:
    # ! Time Limit Exceeded
    return sum(i for i in range(1, num // 2 + 1) if not num % i) == num


def check_perfect_number(num: int) -> bool:
    """
    If m is a divisor of num then "num / m" is also a divisor of num
    """

    if num <= 3:
        return False

    divisors = [1]
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    return sum(divisors) == num


if __name__ == "__main__":
    assert check_perfect_number(28)
    assert not check_perfect_number(7)
    assert not check_perfect_number(99999997)
    assert not check_perfect_number(1)
