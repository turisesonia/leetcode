"""
# 69
Easy
Sqrt(x)

https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
給定一個非負的整數 x , 回傳這個 x 的平方根後無條件捨去的整數

The returned integer should be non-negative as well.
回傳的整數也應該是正數

You must not use any built-in exponent function or operator.
不可使用程式內置的函數或運算符解題

! For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

0 <= x <= 2^^31 - 1
"""


def my_sqrt(x: int) -> int:
    """
    直覺解
    從 1 開始每個小於 x 的數字都互相相乘找是否為平方根
    """
    if x <= 1:
        return x

    prev = None

    for i in range(1, x):
        sq = i * i

        if sq == x:
            return i

        if sq > x:
            break
        else:
            prev = i

    return prev


def my_sqrt(x: int) -> int:
    """
    Use binary search

    Example: x = 900

    0 ~ 450 ~ 900
    0 ~ 225 ~ 450
    0 ~ 112 ~ 225
    0 ~ 56 ~ 112
    0 ~ 28 ~ 56
    28 ~ 42 ~ 56
    28 ~ 35 ~ 42
    28 ~ 31 ~ 35
    28 ~ 29 ~ 31
    29 ~ 30 ~ 31

    Answer is 30
    """

    if x <= 1:
        return x

    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid == left:
            break

        sq = mid * mid

        print(f"left={left}, mid={mid}, right={right}, sq={sq}")

        if sq > x:
            right = mid
        elif sq < x:
            left = mid
        else:
            break

    return mid


if __name__ == "__main__":
    assert my_sqrt(900) == 30
    # assert my_sqrt(1) == 1
    # assert my_sqrt(2) == 1
    # assert my_sqrt(3) == 1
    # assert my_sqrt(4) == 2
    # assert my_sqrt(8) == 2
    # assert my_sqrt(2147483647) == 46340
