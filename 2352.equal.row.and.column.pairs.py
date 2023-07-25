"""
# 2352
Medium
Equal Row and Column Pairs

https://leetcode.com/problems/equal-row-and-column-pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

from typing import List


def equal_pairs(grid: List[List[int]]) -> int:
    print([list(r) for r in zip(*grid)])
    gl = len(grid)

    row_tmp = {}
    col_tmp = {}

    ans = set()

    for i in range(gl):
        row = tuple(grid[i])
        col = tuple(grid[j][i] for j in range(gl))

        row_tmp[row] = i
        col_tmp[col] = i

        j = col_tmp.get(row, -1)
        k = row_tmp.get(col, -1)

        if j >= 0:
            ans.add((i, j))

        if k >= 0:
            ans.add((k, i))

    return len(ans)


if __name__ == "__main__":
    # [2, 7, 7]
    assert (
        equal_pairs(
            [
                [3, 2, 1],
                [1, 7, 6],
                [2, 7, 7],
            ]
        )
        == 1
    )

    # [3, 1, 2, 2],
    # [2, 4, 2, 2],
    # [2, 4, 2, 2],
    assert (
        equal_pairs(
            [
                [3, 1, 2, 2],
                [1, 4, 4, 5],
                [2, 4, 2, 2],
                [2, 4, 2, 2],
            ]
        )
        == 3
    )

    # [3, 1, 2, 2],
    # [2, 4, 2, 2],
    # [2, 4, 2, 2],
    assert (
        equal_pairs(
            [
                [3, 1, 2, 2],
                [1, 4, 4, 4],
                [2, 4, 2, 2],
                [2, 5, 2, 2],
            ]
        )
        == 3
    )

    assert (
        equal_pairs(
            [
                [13, 13],
                [13, 13],
            ]
        )
        == 4
    )
