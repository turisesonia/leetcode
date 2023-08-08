"""
# 119
Easy
Pascal's Triangle II

https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List


def get_row(rowIndex: int) -> List[List[int]]:
    row = [1]

    for i in range(rowIndex):
        arr = [1]

        for j in range(i):
            arr.append(row[j] + row[j + 1])

        arr.append(1)

        row = arr

    return row


if __name__ == "__main__":
    assert get_row(0) == [1]
    assert get_row(1) == [1, 1]
    assert get_row(2) == [1, 2, 1]
    assert get_row(3) == [1, 3, 3, 1]
