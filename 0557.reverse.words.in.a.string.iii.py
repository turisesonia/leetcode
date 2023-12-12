"""
# 557
Easy
Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:
* 1 <= s.length <= 5 * 104
* s contains printable ASCII characters.
* s does not contain any leading or trailing spaces.
* There is at least one word in s.
* All the words in s are separated by a single space.
"""


def reverse_words(s: str) -> str:
    return " ".join(words[::-1] for words in s.split(" "))


if __name__ == "__main__":
    assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverse_words("Mr Ding") == "rM gniD"
