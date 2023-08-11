"""
# 171
Easy
Excel Sheet Column Number

https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


def title_to_number(columnTitle: str) -> int:
    """
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    R = 26

    ABC == R**2 x A{index of alph + 1} + R**1 x B{index of alph + 1} + R**0 x C
    """

    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    str_len = len(columnTitle)

    num = 0
    for i in range(str_len):
        dig = str_len - i - 1

        num += 26**dig * (alph.index(columnTitle[i]) + 1)

    return num


if __name__ == "__main__":
    assert title_to_number("A") == 1
    assert title_to_number("AB") == 28
    assert title_to_number("ZY") == 701
    assert title_to_number("ABABAB") == 12814284
