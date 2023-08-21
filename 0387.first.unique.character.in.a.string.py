"""
# 387
Easy
First Unique Character in a String

https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""


def first_uniq_char(s: str) -> int:
    hm = {}
    uniq = []
    appeared = []

    for i in range(len(s)):
        char = s[i]

        if char not in appeared:
            uniq.append(i)
            appeared.append(char)

        else:
            prev = hm[char]
            if prev in uniq:
                uniq.remove(prev)

        hm[char] = i

    return -1 if not len(uniq) else uniq[0]


if __name__ == "__main__":
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("aabb") == -1
