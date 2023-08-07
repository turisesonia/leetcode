"""
# 118
Easy
Pascal's Triangle

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    result = []
    for i in range(numRows):
        arr = [1]

        if i > 0:
            prev = result[-1]

            for j in range(i - 1):
                arr.append(prev[j] + prev[j + 1])

            arr.append(1)

        result.append(arr)

    return result


if __name__ == "__main__":
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(1) == [[1]]
