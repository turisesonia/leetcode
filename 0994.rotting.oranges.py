"""
# 994
Medium
Rotting Oranges

https://leetcode.com/problems/rotting-oranges

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell.
- 1 representing a fresh orange.
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:

https://assets.leetcode.com/uploads/2019/02/16/oranges.png

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh_remain = 0
        visited = {}
        rottings = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if val == 1:
                    fresh_remain += 1
                    visited[(i, j)] = False

                elif val == 2:
                    rottings.append((i, j, 0))
                    visited[(i, j)] = True

        while rottings:
            i, j, minutes = rottings.pop(0)

            # up
            if i > 0:
                val = grid[i - 1][j]
                if val == 1 and not visited[(i - 1, j)]:
                    visited[(i - 1, j)] = True
                    fresh_remain -= 1
                    rottings.append((i - 1, j, minutes + 1))

            # down
            if i < m - 1:
                val = grid[i + 1][j]
                if val == 1 and not visited[(i + 1, j)]:
                    visited[(i + 1, j)] = True
                    fresh_remain -= 1
                    rottings.append((i + 1, j, minutes + 1))

            # left
            if j > 0:
                val = grid[i][j - 1]
                if val == 1 and not visited[(i, j - 1)]:
                    visited[(i, j - 1)] = True
                    fresh_remain -= 1
                    rottings.append((i, j - 1, minutes + 1))

            # right
            if j < n - 1:
                val = grid[i][j + 1]
                if val == 1 and not visited[(i, j + 1)]:
                    visited[(i, j + 1)] = True
                    fresh_remain -= 1
                    rottings.append((i, j + 1, minutes + 1))

        return -1 if fresh_remain > 0 else minutes


if __name__ == "__main__":
    solution = Solution()

    minutes = solution.orangesRotting(
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]
    )
    assert minutes == 4

    minutes = solution.orangesRotting(
        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1],
        ]
    )
    assert minutes == -1

    minutes = solution.orangesRotting([[0, 2]])
    assert minutes == 0

    minutes = solution.orangesRotting(
        [
            [2, 1, 1],
            [1, 1, 1],
            [0, 1, 2],
        ]
    )
    assert minutes == 2

    minutes = solution.orangesRotting([[0]])
    assert minutes == 0
