"""
# 500
Easy
Keyboard Row

https://leetcode.com/problems/keyboard-row/

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""


def find_words(words: list[str]) -> list[str]:
    keyboards = {}
    for letter in "qwertyuiop":
        keyboards[letter] = 1
    for letter in "asdfghjkl":
        keyboards[letter] = 2
    for letter in "zxcvbnm":
        keyboards[letter] = 3

    ans = []
    for word in words:
        same = None
        for char in word:
            row = keyboards[char.lower()]

            if same is not None and row != same:
                break
            else:
                same = row
        else:
            ans.append(word)

    return ans


if __name__ == "__main__":
    assert find_words(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    assert find_words(["omk"]) == []
    assert find_words(["adsdf", "sfd"]) == ["adsdf", "sfd"]
