"""
# 344
Easy
Reverse String

https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Example 2:
Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""


def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    for i in range(len(s) // 2):
        # indexes from end to beginning
        j = len(s) - i - 1

        s[i], s[j] = s[j], s[i]


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]

    s = ["a", "p", "p", "l", "e"]
    reverse_string(s)
    assert s == ["e", "l", "p", "p", "a"]

    s = [
        "A",
        " ",
        "m",
        "a",
        "n",
        ",",
        " ",
        "a",
        " ",
        "p",
        "l",
        "a",
        "n",
        ",",
        " ",
        "a",
        " ",
        "c",
        "a",
        "n",
        "a",
        "l",
        ":",
        " ",
        "P",
        "a",
        "n",
        "a",
        "m",
        "a",
    ]
    reverse_string(s)
    assert s == [
        "a",
        "m",
        "a",
        "n",
        "a",
        "P",
        " ",
        ":",
        "l",
        "a",
        "n",
        "a",
        "c",
        " ",
        "a",
        " ",
        ",",
        "n",
        "a",
        "l",
        "p",
        " ",
        "a",
        " ",
        ",",
        "n",
        "a",
        "m",
        " ",
        "A",
    ]
