"""
# 434
Easy
Number of Segments in a String

https://leetcode.com/problems/number-of-segments-in-a-string/description/

Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1

Constraints:
0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
"""


def count_segments(s: str) -> int:
    res = 0
    segment = ""

    for c in s:
        if c == " ":
            if len(segment) > 0:
                res += 1

            segment = ""

        else:
            segment += c

    if len(segment) > 0:
        res += 1

    return res


def count_segments(s: str) -> int:
    # Using built-in library in python
    return len(s.split())


if __name__ == "__main__":
    assert count_segments("Hello, my name is John") == 5
    assert count_segments("Hello") == 1
    assert count_segments("") == 0
