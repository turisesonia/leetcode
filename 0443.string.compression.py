"""
# 443
Medium
String Compression

https://leetcode.com/problems/string-compression/

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.


Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

from typing import List


def compress(chars: List[str]) -> int:
    """
    two pointer 解
    """
    n = len(chars)
    i = 0
    j = i + 1
    count = 1
    res = ""

    while j <= n:
        if j < n and chars[i] == chars[j]:
            count += 1
            j += 1

        else:
            res += chars[i]
            if count > 1:
                res += str(count)

            i = j
            j = i + 1
            count = 1

    for j in range(len(res)):
        chars[j] = res[j]

    return len(res)


if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert compress(chars) == 6
    # assert chars == ["a", "2", "b", "2", "c", "3"]

    chars = ["a"]
    assert compress(["a"]) == 1
    # assert chars == ["a"]

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert compress(chars) == 4
    # assert chars == ["a", "b", "1", "2"]

    chars = ["a", "a", "a", "b", "b", "a", "a"]
    assert compress(chars) == 6
    # assert chars == ["a", "3", "b", "2", "a", "2"]
