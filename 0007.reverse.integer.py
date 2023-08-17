"""
#7
Reverse Integer
Medium

https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-2**31 <= x <= 2**31 - 1
"""


def reverse(x: int) -> int:
    # 判斷原值 x 是否為負數
    negative = -1 if x < 0 else 1
    x = str(abs(x))
    ls = []

    # 將 x 轉為字串後, 由右往左依序存進 list 內, 如果遇到第一個為 0 則跳過
    for i in range(len(x) - 1, -1, -1):
        if len(ls) == 0 and x[i] == 0:
            continue

        ls.append(x[i])

    # 將結果轉為 int
    res = int("".join(ls)) * negative

    # 題目限制
    if res not in range(-(2**31), 2**31):
        return 0

    return res


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(274839291) == 192938472
    assert reverse(120) == 21
    assert reverse(1200) == 21
    assert reverse(0) == 0
    assert reverse(1534236469) == 0