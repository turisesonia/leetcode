"""
# 383
Easy
Ransom Note

https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


def can_construct(ransomNote: str, magazine: str) -> bool:
    hm = {}
    for m in magazine:
        hm[m] = hm.get(m, 0) + 1

    for r in ransomNote:
        if r not in magazine or hm[r] <= 0:
            return False

        hm[r] -= 1

    return True


# def can_construct(ransomNote: str, magazine: str) -> bool:
#     hm = {}

#     for r in ransomNote:
#         if r not in magazine:
#             return False

#         if r not in hm:
#             hm[r] = magazine.count(r)

#         if hm[r] <= 0:
#             return False

#         hm[r] -= 1

#     return True


if __name__ == "__main__":
    assert not can_construct("a", "b")
    assert not can_construct("aa", "ab")
    assert can_construct("aa", "aab")
