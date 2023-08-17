"""
# 338
Counting Bits
Easy

https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
6 --> 110
7 --> 111
8 --> 1000
9 --> 1001

Constraints:
0 <= n <= 105

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""


def count_bits(n: int) -> list[int]:
    res = []

    for i in range(n + 1):
        if i <= 1:
            res.append(i)
            continue

        if i % 2 == 0:
            pass
        else:
            res.append(res[i - 1] + 1)

    return res


def count_bits(n: int) -> list[int]:
    res = [0 for _ in range(n + 1)]
    print(res)
    prev = 2

    for i in range(n + 1):
        if i <= 1:
            res[i] = i
            continue

        if i % 2 == 0:
            prev = i

        print(i, prev)
        res[i] = res[i - prev] + 1

    print("------", n, " : ", res)
    return res


def count_bits(n: int) -> list[int]:
    if n == 0:
        return [0]

    dp = [0] * (n + 1)

    print(dp)
    dp[0] = 0
    dp[1] = 1
    low = 2
    for i in range(2, n + 1):
        if i % low == 0:
            low = i
        dp[i] = dp[i - low] + 1

    print("------", n, " : ", dp)
    return dp


if __name__ == "__main__":
    assert count_bits(2) == [0, 1, 1]
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
    assert count_bits(6) == [0, 1, 1, 2, 1, 2, 2]
    assert count_bits(7) == [0, 1, 1, 2, 1, 2, 2, 3]
