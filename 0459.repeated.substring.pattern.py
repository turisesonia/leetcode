"""
# 459
Easy
Repeated Substring Pattern

https://leetcode.com/problems/repeated-substring-pattern/

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""


def repeated_substring_pattern(s: str) -> bool:
    l = len(s)

    for i in range(1, l // 2 + 1):
        # length 整除 i 才判斷是否可以組成
        if l % i == 0:
            if s[:i] * (l // i) == s:
                return True

    return False


if __name__ == "__main__":
    assert not repeated_substring_pattern("a")
    assert repeated_substring_pattern("abab")
    assert not repeated_substring_pattern("aba")
    assert repeated_substring_pattern("abcabcabcabc")
