"""
# 242
Easy
Valid Anagram

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram(s: str, t: str) -> bool:
    ls, lt = len(s), len(t)

    if ls != lt:
        return False

    hash_s = {}
    hash_t = {}

    for i in range(ls):
        if s[i] not in hash_s:
            hash_s[s[i]] = 1
        else:
            hash_s[s[i]] += 1

        if t[i] not in hash_t:
            hash_t[t[i]] = 1
        else:
            hash_t[t[i]] += 1

    return hash_s == hash_t


def is_anagram(s: str, t: str) -> bool:
    """
    One hash map solution
    """
    ls, lt = len(s), len(t)
    if ls != lt:
        return False

    hm = {}

    for i in range(ls):
        s_ = s[i]
        t_ = t[i]

        hm[s_] = 1 + hm.get(s_, 0)
        hm[t_] = -1 + hm.get(t_, 0)

    for n in hm.values():
        if n != 0:
            return False

    return True


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")
