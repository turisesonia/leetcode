"""
# 441
Easy
Arranging Coins

https://leetcode.com/problems/arranging-coins/

You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins.
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 231 - 1
"""


def arrange_coins(n: int) -> int:
    total = 0
    rows = 0

    for i in range(1, n + 1):
        total += i

        if total > n:
            break
        else:
            rows += 1

    return rows


def arrange_coins(n: int) -> int:
    """
    Solved using Binary search
    """
    if n == 1:
        return 1

    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2

        if (1 + mid) * mid / 2 <= n:
            left = mid
        else:
            right = mid

    return left


if __name__ == "__main__":
    assert arrange_coins(5) == 2
    assert arrange_coins(8) == 3
