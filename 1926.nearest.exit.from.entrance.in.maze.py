"""
# 1926
Medium
Nearest Exit from Entrance in Maze

https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze.
Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:

https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg

Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:

https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:

https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.


Constraints:
- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- maze[i][j] is either '.' or '+'.
- entrance.length == 2
- 0 <= entrancerow < m
- 0 <= entrancecol < n
- entrance will always be an empty cell.
"""

from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits = set()

        # find all exit cells except entrance cell
        for ri, row in enumerate(maze):
            for ci, col in enumerate(row):
                if [ri, ci] == entrance:
                    continue

                if (ri == 0 or ri == len(maze) - 1) and col == ".":
                    exits.add((ri, ci))

                if (ci == 0 or ci == len(row) - 1) and col == ".":
                    exits.add((ri, ci))

        # store visited cell
        visited = {(entrance[0], entrance[1])}

        # BFS queue
        queue = [(entrance[0], entrance[1], 0)]

        while queue:
            y, x, steps = queue.pop(0)

            if (y, x) in exits:
                return steps

            # up
            if y - 1 >= 0:
                self.move((y - 1, x), steps, maze, queue, visited)

            # down
            if y + 1 < len(maze):
                self.move((y + 1, x), steps, maze, queue, visited)

            # left
            if x - 1 >= 0:
                self.move((y, x - 1), steps, maze, queue, visited)

            # right
            if x + 1 < len(maze[0]):
                self.move((y, x + 1), steps, maze, queue, visited)

        return -1

    def move(self, cell: tuple[int, int], steps: int, maze: list, queue: list, visited: set):
        if cell not in visited and maze[cell[0]][cell[1]] == ".":
            visited.add(cell)
            queue.append((cell[0], cell[1], steps + 1))


if __name__ == "__main__":
    solution = Solution()

    steps = solution.nearestExit(
        maze=[
            ["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."],
        ],
        entrance=[1, 2],
    )
    assert steps == 1

    steps = solution.nearestExit(
        maze=[
            ["+", "+", "+"],
            [".", ".", "."],
            ["+", "+", "+"],
        ],
        entrance=[1, 0],
    )
    assert steps == 2

    steps = solution.nearestExit(maze=[[".", "+"]], entrance=[0, 0])
    assert steps == -1

    steps = solution.nearestExit(
        maze=[
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", ".", "+"],
        ],
        entrance=[0, 1],
    )

    assert steps == 12

    steps = solution.nearestExit(
        maze=[
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", "+", "."],
        ],
        entrance=[0, 1],
    )
