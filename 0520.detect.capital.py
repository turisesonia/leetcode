"""
# 520
Easy
Detect Capital

https://leetcode.com/problems/detect-capital/description/

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


def detect_capital_use(word: str) -> bool:
    if len(word) <= 1:
        return True

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if word[0] in lower:
        st = 1
        invalid = upper
    elif word[0] in upper and word[1] in lower:
        st = 2
        invalid = upper
    else:
        st = 1
        invalid = lower

    for char in word[st:]:
        if char in invalid:
            return False

    return True


def detect_capital_use(word: str):
    """
    python solution
    """

    return word in (word.lower(), word.upper(), word.title())


if __name__ == "__main__":
    assert detect_capital_use("USA")
    assert not detect_capital_use("FlaG")
    assert detect_capital_use("Google")
    assert detect_capital_use("leetcode")
    assert not detect_capital_use("hellO")
    assert detect_capital_use("G")
