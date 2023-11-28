"""
# 62
Medium
Unique Paths

https://leetcode.com/problems/unique-paths

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:

https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
* 1 <= m, n <= 100
"""


def unique_paths(m: int, n: int) -> int:
    """
    Math combination formula
    C n 取 m = n! / (m! * (n-m)!)

    數學解法, m * n 階的 grid
    要從左上走到右下且一次只能一步向右或向下走
    總共會走的路徑長度為 (m - 1) + (n - 1)

    以 m = 3, n = 7 為例
    總共走的路徑只會有 8 步，即向右 2 步 + 向下 6 步
    找出這樣走法的所有組合就為答案

    用數學公式 C m 取 n 找出有多少組合
    """
    total = m + n - 2
    items = min(m - 1, n - 1)

    def factorial(num: int):
        n = 1
        for i in range(1, num + 1):
            n *= i

        return n

    return int(factorial(total) / (factorial(items) * factorial(total - items)))


def unique_paths(m: int, n: int) -> int:
    """
    Dynamic Programming
    [
        [s, 1, 1, 1, 1, 1, 1]
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 6, 10, 15, 21, 28],
    ]

    除了第一列或第一行都只有一種走法，
    要走到其餘位置的走法數量為 => 該位置的上面一個位置走法數量 + 該位置左邊一個位置走法數量
    以此類推，就可以找到走到右下的走法數量
    """
    lookup = {}

    def find(m: int, n: int, lookup: dict):
        if m == 1 or n == 1:
            return 1

        k = (m, n)
        if lookup.get(k) == None:
            lookup[k] = find(m - 1, n, lookup) + find(m, n - 1, lookup)

        return lookup[k]

    res = find(m, n, lookup)
    return res


if __name__ == "__main__":
    assert unique_paths(m=3, n=7) == 28
    assert unique_paths(m=3, n=2) == 3
