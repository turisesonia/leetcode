"""
# 14
Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


def longest_common_prefix(strs: list):
    res = ""

    for chars in zip(*strs):

        if len(set(chars)) != 1:
            break

        res += chars[0]

    return res


def longest_common_prefix_2(strs: list):
    res = strs[0]

    for string in strs:
        while not string.startswith(res):
            res = res[0:-1]

    return res

if __name__ == "__main__":

    assert "fl" == longest_common_prefix(["flower", "flow", "flight"])
    assert "" == longest_common_prefix(["dog", "racecar", "car"])
    assert "" == longest_common_prefix([""])
