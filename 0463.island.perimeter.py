"""
# 463
Easy
Island Perimeter

https://leetcode.com/problems/island-perimeter/

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Image:
https://assets.leetcode.com/uploads/2018/10/12/island.png

Example 1:
Input: grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""


def island_perimeter(grid: list[list[int]]) -> int:
    row_len = len(grid)
    col_len = len(grid[0])

    per = 0
    i, j = 0, 0

    while i < row_len:
        for j in range(col_len):
            if not grid[i][j]:
                continue

            # top
            if i == 0 or i > 0 and not grid[i - 1][j]:
                per += 1

            # left
            if j == 0 or j > 0 and not grid[i][j - 1]:
                per += 1

            # right
            if j == col_len - 1 or j < col_len - 1 and not grid[i][j + 1]:
                per += 1

            # bottom
            if i == row_len - 1 or i < row_len - 1 and not grid[i + 1][j]:
                per += 1

        i += 1

    return per


if __name__ == "__main__":
    assert island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    assert island_perimeter([[1]]) == 4
    assert island_perimeter([[1, 0]]) == 4
