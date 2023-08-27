"""
# 461
Easy
Hamming Distance

https://leetcode.com/problems/hamming-distance/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2^31 - 1
"""


def hamming_distance(x: int, y: int) -> int:
    return f"{x^y:0b}".count("1")


if __name__ == "__main__":
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(3, 1) == 1
