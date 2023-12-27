"""
# 36
Medium
Valid Sudoku

https://leetcode.com/problems/valid-sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
* board.length == 9
* board[i].length == 9
* board[i][j] is a digit 1-9 or '.'.
"""


def is_valid_sudoku(board: list[list[str]]) -> bool:
    hm = {}

    for ri, row in enumerate(board):
        row_key = ("row", ri)
        if row_key not in hm:
            hm[row_key] = set()

        for ci, num in enumerate(row):
            col_key = ("col", ci)
            if col_key not in hm:
                hm[col_key] = set()

            # every sub 3x3 box
            box_key = ("box", ri // 3, ci // 3)
            if box_key not in hm:
                hm[box_key] = set()

            if num == ".":
                continue

            if num in hm[row_key] or num in hm[col_key] or num in hm[box_key]:
                return False

            hm[row_key].add(num)
            hm[col_key].add(num)
            hm[box_key].add(num)

    return True


if __name__ == "__main__":
    assert is_valid_sudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    assert not is_valid_sudoku(
        board=[
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    w = {
        ("row", 0): {"5", "7", "3"},
        ("col", 0): {"5", "7", "6", "8", "4"},
        ("col", 1): {"9", "6", "3"},
        ("col", 2): {"8"},
        ("col", 3): {"1", "8", "4"},
        ("col", 4): {"1", "7", "6", "8", "9", "2"},
        ("col", 5): {"9", "5", "3"},
        ("col", 6): {"2"},
        ("col", 7): {"6", "7", "8"},
        ("col", 8): {"1", "5", "6", "3", "9"},
        ("row", 1): {"9", "1", "5", "6"},
        ("row", 2): {"9", "6", "8"},
        ("row", 3): {"6", "8", "3"},
        ("row", 4): {"1", "3", "8", "4"},
        ("row", 5): {"2", "6", "7"},
        ("row", 6): {"2", "6", "8"},
        ("row", 7): {"9", "1", "5", "4"},
        ("row", 8): {"9", "7", "8"},
    }
