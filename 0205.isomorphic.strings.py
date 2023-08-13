"""
# 205
Easy
Isomorphic Strings
同構字串

https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

檢查 s 可以轉換成 t, 且 t 也可以轉換成 s

1. (s, t) = (paper, title) 為例

(paper, title) = {p: t, a: i, e: l, r: e}
(title, paper) = {t: p, i: a, l: e, r: e}

所以 (paper, title) 為 Isomorphic

2. (s, t) = (badc, baba)
(badc, baba) = {b: b, a: a, d: b, c: a}
(baba, badc) = {b: b, a: a}
=> 判斷到第二個 b 時, b = d 但前一個已經將 b 轉換為 b 了, 所以這個 case 就不是 ismorphic
"""


def is_isomorphic(s: str, t: str) -> bool:
    hash_s = {}
    hash_t = {}

    i = 0

    while i < len(s):
        ss = s[i]
        tt = t[i]

        if ss not in hash_s:
            hash_s[ss] = tt

        if tt not in hash_t:
            hash_t[tt] = ss

        if hash_s[ss] != tt or hash_t[tt] != ss:
            return False

        i += 1

    return True


if __name__ == "__main__":
    assert is_isomorphic("egg", "add")
    assert not is_isomorphic("foo", "bar")
    assert is_isomorphic("paper", "title")
    assert not is_isomorphic("bbbaaaba", "aaabbbba")
    assert not is_isomorphic("badc", "baba")
