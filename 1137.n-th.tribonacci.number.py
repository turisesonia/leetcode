"""
# 1137
Easy
N-th Tribonacci Number

https://leetcode.com/problems/n-th-tribonacci-number

The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


def tribonacci(n: int) -> int:
    """
    seq = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    """
    seq = [0, 1, 1]

    if n <= 2:
        return seq[n]

    for i in range(3, n + 1):
        v = seq[i - 3] + seq[i - 2] + seq[i - 1]

        seq.append(v)

    return v


if __name__ == "__main__":
    assert tribonacci(4) == 4
    assert tribonacci(25) == 1389537
