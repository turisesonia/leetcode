"""
# 14
Easy
Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def valid_parentheses(s: str):
    if len(s) % 2 != 0:
        return False

    open_chars = ["(", "[", "{"]
    correct = {")": "(", "]": "[", "}": "{"}

    # 使用 list 堆疊
    # 將開始括號符存入 list, 如果遇到關閉符號
    # 從堆疊中取出最後一個欄位來比對是否為合法的括號開關
    tmp = []

    for char in s:
        if char in open_chars:
            tmp.append(char)

        else:
            if len(tmp) == 0 or correct[char] != tmp.pop():
                return False

    return len(tmp) == 0


if __name__ == "__main__":
    assert valid_parentheses("()")
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")
    assert valid_parentheses("{[]}")
