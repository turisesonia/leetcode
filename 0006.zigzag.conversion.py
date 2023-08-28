"""
# 6
Medium
Zigzag Conversion

https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


def convert(s: str, numRows: int) -> str:
    """
    numRows = 4
    # completed column index
    k = numRows - 1

    要產生之字形的序列

    0 4 08 12 16 20 24    00 xx xx 12 xx xx 24
    1 5 09 13 17 21 25 => 01 xx 09 13 xx 21 25
    2 6 10 14 18 22 26    02 06 xx 14 18 xx 26
    3 7 11 15 19 23 27    03 xx xx 15 xx xx 27

    依照上圖，

    完整 column 的公式為 column_index % k == 0 (column index 整除 k)
    不完整 column 跳過的數量為 k - (column index % k)
    """
    s_len = len(s)

    if s_len == 1 or numRows == 1:
        return s

    i = 0
    k = numRows - 1

    rows = []
    row = []

    while i < s_len:
        c = s[i]

        if len(row) == numRows:
            rows.append(row)
            row = []

        rowsl = len(rows)

        # full column
        if rowsl % k == 0:
            row.append(c)

        else:
            skip = k - (rowsl % k)

            zig_row = ["" if j != skip else c for j in range(numRows)]
            rows.append(zig_row)

        i += 1

    if len(row) > 0:
        for _ in range(numRows - len(row)):
            row.append("")

        rows.append(row)

    print(rows)

    res = ""
    a, b = 0, 0

    while b < numRows:
        while a < len(rows):
            res += rows[a][b]
            a += 1

        a = 0
        b += 1

    print(res)
    return res


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    # Initialize rows as empty strings
    rows = ["" for _ in range(numRows)]
    """
    [
        "",
        "",
        "",
    ]
    """

    n = len(s)
    i = 0  # index for string s

    while i < n:
        # Go down vertically
        for row in range(numRows):
            """
            [
                "P",
                "A",
                "Y",
            ]
            """
            if i < n:
                rows[row] += s[i]
                i += 1

        # Go up diagonally
        for row in range(numRows - 2, 0, -1):  # Skip the first and last rows
            """
            [
                "P",      "P"
                "A",  =>  "AP"
                "Y",      "Y"
            ]
            """
            if i < n:
                rows[row] += s[i]
                i += 1

    # Concatenate all rows to get the final string
    return "".join(rows)


if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("AB", 1) == "AB"
