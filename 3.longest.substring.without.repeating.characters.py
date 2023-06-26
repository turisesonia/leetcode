"""
# 3
Medium
Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


# v1
def length_of_longest_substring(s: str) -> int:
    """
    用堆疊解, 將每個字母存進 list, 當有遇到重複時,
    從頭拿出字母直到重複的被拿出來為止

    Args:
        s (str): _description_

    Returns:
        int: _description_
    """
    stack = []
    length = 0

    for char in s:
        while char in stack:
            stack.pop(0)

        stack.append(char)

        length = len(stack) if len(stack) > length else length

    return length


# v2
def length_of_longest_substring(s: str):
    """
    遇到重複的字母時, 找出次重複字母所在文字的位置, 從該位置重新產生 substr

    Args:
        s (str): _description_

    Returns:
        int: _description_
    """
    res = ""
    length = 0

    for char in s:
        if char in res:
            idx = res.index(char) + 1
            res = res[idx:]

        res += char

        length = len(res) if len(res) > length else length

    return length


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("ekqodkje") == 6
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("au") == 2
    assert length_of_longest_substring("bbtablud") == 6
    assert length_of_longest_substring("bpfbhmipx") == 7
