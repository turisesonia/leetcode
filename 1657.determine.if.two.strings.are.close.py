"""
# 1657
Medium
Determine if Two Strings Are Close

https://leetcode.com/problems/determine-if-two-strings-are-close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""


class Solution:
    """
    解這題時，給定的兩個操作其實不用真的實作出來
    根據他給的兩個操作判斷，可以得知只需要判斷這兩個字串是否符合以下三點
    1. 字串長度相等
    2. 字串內出現的字母要一致
    3. 字母重複出現的次數要相同 (ex: aabbbcc a:2, b:3, c:2 / aaabbcc a:3, b:2, c:2)
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        len1, len2 = len(word1), len(word2)

        if len1 != len2:
            return False

        if set(word1) != set(word2):
            return False

        wc1 = {}
        wc2 = {}

        for i in range(len1):
            if word1[i] not in wc1:
                wc1[word1[i]] = 1
            else:
                wc1[word1[i]] += 1

            if word2[i] not in wc2:
                wc2[word2[i]] = 1
                pass
            else:
                wc2[word2[i]] += 1

        if sorted(wc1.values()) != sorted(wc2.values()):
            return False

        return True

    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        利用 Python Counter 計算出現過的字母及次數
        """

        from collections import Counter

        if len(word1) != len(word2):
            return False

        wc1 = Counter(word1)
        wc2 = Counter(word2)

        if sorted(wc1.keys()) == sorted(wc2.keys()) and sorted(wc1.values()) == sorted(
            wc2.values()
        ):
            return True

        return False


if __name__ == "__main__":
    su = Solution()

    assert su.closeStrings("abc", "bca")
    assert not su.closeStrings("a", "aa")
    assert su.closeStrings("cabbba", "abbccc")
    assert not su.closeStrings("abbzzca", "babzzcz")
