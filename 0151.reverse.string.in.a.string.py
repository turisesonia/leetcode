"""
# 151
Medium
Reverse Words in a String

https://leetcode.com/problems/reverse-words-in-a-string

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""


def reverse_words(s: str) -> str:
    """
    將字串依照 " " 一格空格做分割, 判斷裡面的每個單字
    如果是空字串或空格就跳過
    將合乎規則的單字 left append 至 reverse array (為了倒序)

    return " ".join(reverse)
    """
    reverse = []
    for word in s.split(" "):
        if word == " " or len(word) <= 0:
            continue

        reverse.insert(0, word)

    return " ".join(reverse)


def reverse_words(s: str) -> str:
    """
    Python 3 專用解, split 不帶任何參數會自動把多餘的空格都刪掉
    """
    s = s.split()
    s.reverse()

    return " ".join(s)


if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("  hello world  ") == "world hello"
