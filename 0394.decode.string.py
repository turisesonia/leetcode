"""
# 394
Medium
Decode String

https://leetcode.com/problems/decode-string

Given an encoded string, return its decoded string.
給定一個編碼過的字串，回傳已解碼後的結果

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
編碼的規則是: k[encoded_string] 中括號內的字串代表要被重複的字串，而 k 為要重複的次數

Note that k is guaranteed to be a positive integer.
k 保證一定是正數

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


def decode_string(s: str) -> str:
    stack = []
    for c in s:
        if c.isnumeric():
            stack.append(int(c))

        pass


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
