"""
# 509
Easy
Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30
"""


def fib(n: int) -> int:
    fib = [0, 1]

    if n <= 1:
        return fib[n]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]


if __name__ == "__main__":
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3