"""
# 290
Easy
Word Pattern

https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1. 1 <= pattern.length <= 300
2. pattern contains only lower-case English letters.
3. 1 <= s.length <= 3000
4. s contains only lowercase English letters and spaces ' '.
5. s does not contain any leading or trailing spaces.
6. All the words in s are separated by a single space.

Problem description is not clear, here is a better description

Given a pattern and a string s, find if s follows the same pattern.

pattern and s are same if:
1  Each character in pattern represents a word in s
2. No two distinct characters in pattern can represent the same word in s
3. No single character in pattern can represent two distinct words in s.
"""


def word_pattern(pattern: str, s: str) -> bool:
    s = s.split(" ")

    # return False if pattern and s has different lengths
    if len(pattern) != len(s):
        return False

    hm = {}

    # compare each char in pattern and with the words in s one by one
    for i in range(len(pattern)):
        p = pattern[i]

        if p not in hm:
            if s[i] not in hm.values():
                hm[p] = s[i]
            else:
                return False

        else:
            if hm[p] != s[i]:
                return False

    return True


if __name__ == "__main__":
    assert word_pattern("abba", "dog cat cat dog")
    assert not word_pattern("abba", "dog cat cat fish")
    assert not word_pattern("aaaa", "dog cat cat dog")
    assert not word_pattern("abba", "dog dog dog dog")
