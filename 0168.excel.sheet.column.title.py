"""
# 168
Easy
Excel Sheet Column Title

https://leetcode.com/problems/excel-sheet-column-title/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 231 - 1
"""

# def convert_title_int(title: str) -> int:
#     alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     str_len = len(title)

#     num = 0
#     for i in range(str_len):
#         dig = str_len - i - 1

#         num += 26**dig * (alph.index(title[i]) + 1)

#     return num


# if __name__ == "__main__":
#     assert convert_title_int("A") == 1
#     assert convert_title_int("AB") == 28
#     assert convert_title_int("ZY") == 701
#     assert convert_title_int("ABABAB") == 12814284


def convert_to_title(columnNumber: int) -> str:
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    mod = columnNumber % 26
    print(mod)
    columnNumber -= mod

    times = 0

    while columnNumber > 0:
        print('--', columnNumber)
        columnNumber = columnNumber // 26
        times += 1

    print(times, mod)

    return alph[mod - 1]


if __name__ == "__main__":
    # assert convert_to_title(1) == "A"
    # assert convert_to_title(28) == "AB"
    # assert convert_to_title(701) == "ZY"
    assert convert_to_title(12814284) == "ABABAB"
