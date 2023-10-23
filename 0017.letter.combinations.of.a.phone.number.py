"""
# 17
Medium
Letter Combinations of a Phone Number

https://leetcode.com/problems/letter-combinations-of-a-phone-number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List


# solution version 1
class Solution:
    tables = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        if len(digits) > 0:
            # 處理第一個數字, ex: "2" -> ans = ["a, b, c"]
            for alph in self.tables[digits[0]]:
                ans.append(alph)

            # 後續還有數字傳下一個數字及答案繼續處理
            self.dfs(digits[1:], ans)

        return ans

    def dfs(self, digits: str, ans: list):
        if not digits:
            return

        # 計算上一層輸入進來時，有多少前置文字
        times = len(ans)
        for _ in range(times):
            prev = ans.pop(0)
            for alph in self.tables[digits[0]]:
                ans.append(prev + alph)

        self.dfs(digits[1:], ans)


# Solution version 2
class Solution:
    tables = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        if len(digits) > 0:
            self.dfs(digits, "", ans)

        return ans

    def dfs(self, digits: str, prefix: str, ans: list):
        if not digits:
            ans.append(prefix)
            return

        for alph in self.tables[digits[0]]:
            combination = prefix + alph
            self.dfs(digits[1:], combination, ans)


if __name__ == "__main__":
    sol = Solution()

    assert set(sol.letterCombinations("23")) == {
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    }

    assert sol.letterCombinations("") == []

    assert sol.letterCombinations("2") == ["a", "b", "c"]
