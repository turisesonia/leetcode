"""
# 5
Longest Palindromic Substring
Medium

https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindrome(s: str) -> str:
    """
    # 自己解的第一版

    從最長的字串開始判斷是否為 palindrome, 如果是就直接返回結果
    問題是當如果遇到很長的字串但只有非常短的 palindrome 會造成要跑非常久

    # 流程
    Ex: babad
    依照長度分出以下的字串
    babad, baba, abad, bab, aba, bad, ba, ab, ba, ad
    由左至右找是否為 palindrome 如果是就回傳字串
    """
    length = current = len(s)

    while current > 0:
        for i in range(length - current + 1):
            partial = s[i : current + i]

            if partial == partial[::-1]:
                return partial

        current -= 1

    return ""


def longest_palindrome(s: str) -> str:
    """
    Leetcode 解答

    有兩種情況, 字串長度分為奇數及偶數
    - 奇數 ex: a, aba, abcba
    - 偶數 ex: aa, abba, abccba
    由上面範例可以看出這兩種的差異在中間值的位置是 1 或 2 個字母,
    並且從中間值向左右擴散出去的字母都必須相同.

    滿足以上條件就是 palindrome
    """

    def expend(left: int, right: int):
        """
        檢查傳進來的字母 index,
        - left 要大於等於 0, 即向左移動時不可以超出字串第一個字母
        - right 要小於字串長度, 即向右移動不可以超出字串最後一個字母
        - 這兩個 index 的字母必須相同
        符合以上三點就是 palindrome

        當遇到不符合的時候就中止 while 迴圈並回傳上一輪的部分字串
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]

    # 結果, 如果檢查結果的長度大於此文字, 則覆蓋過去
    res = ""

    # 因為要找出最長的 palindrome 所以每一次必須奇數偶數情況同時檢查
    for i in range(len(s)):
        # 奇數情況
        p1 = expend(i, i)
        if len(p1) > len(res):
            res = p1

        # 偶數情況
        p2 = expend(i, i + 1)
        if len(p2) > len(res):
            res = p2

    return res


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ccd") == "cc"
