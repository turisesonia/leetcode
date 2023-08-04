"""
# 28
Easy
Find the Index of the First Occurrence in a String

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
給定兩個字串 needle 和 haystack, 回傳索引值為第一次 needle 等於部分的 haystack, 如果都不符合則回傳 -1

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
haystack and needle consist of only lowercase English characters.
1 <= haystack.length, needle.length <= 104
"""


def str_str(haystack: str, needle: str) -> int:
    i, j = 0, len(needle)

    while j <= len(haystack):
        if haystack[i:j] == needle:
            return i

        i += 1
        j += 1

    return -1


if __name__ == "__main__":
    assert str_str("sadbutsad", "sad") == 0
    assert str_str("leetcode", "leeto") == -1
    assert str_str("a", "a") == 0
    assert str_str("mississippi", "issip") == 4
