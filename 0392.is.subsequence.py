"""
# 392
Easy
Is Subsequence

https://leetcode.com/problems/is-subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
* 0 <= s.length <= 100
* 0 <= t.length <= 10^4
* s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence.
In this scenario, how would you change your code?
"""


def is_subsequence(s: str, t: str) -> bool:
    sl, tl = len(s), len(t)
    si, ti = 0, 0

    res = ""

    while si < sl and ti < tl:
        if s[si] == t[ti]:
            res += t[ti]
            si += 1

        ti += 1

    return res == s


def is_subsequence(s: str, t: str) -> bool:
    # two pointers, i is position of s, j is position of t
    i, j = 0, 0
    sl, tl = len(s), len(t)

    while i < sl and j < tl:
        # get same character, move i one position to the right
        if s[i] == t[j]:
            i += 1

        # move j
        j += 1

    # check i is move to the end
    return i == sl


if __name__ == "__main__":
    assert is_subsequence("abc", "ahbgdc")
    assert not is_subsequence("axc", "ahbgdc")
    assert not is_subsequence("aaaaaa", "bbaaaa")
