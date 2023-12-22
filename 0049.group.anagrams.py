"""
# 49
Medium
Group Anagrams

https://leetcode.com/problems/group-anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

* 1 <= strs.length <= 10^4
* 0 <= strs[i].length <= 10^0
* strs[i] consists of lowercase English letters.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    hm = {}
    results = []

    for str_ in strs:
        key = tuple(sorted(str_))

        if key not in hm:
            results.append([])
            hm[key] = len(results) - 1

        results[hm[key]].append(str_)

    return results


if __name__ == "__main__":
    group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    group_anagrams(strs=[""])
    group_anagrams(strs=["a"])
