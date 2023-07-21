"""
# 1456
Medium
Maximum Number of Vowels in a Substring of Given Length

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


def max_vowels(s: str, k: int) -> int:
    """
    暴力解, 每 k 個 substring 都檢查一次最大含有母音的長度
    """
    vowels = "aeiou"

    l = len(s)
    i = 0

    max_ = 0

    while i < l - k + 1:
        t = 0
        for c in s[i : i + k]:
            if c in vowels:
                t += 1

        if t == k:
            max_ = k
            break

        max_ = max(max_, t)

        i += 1

    return max_


def max_vowels(s: str, k: int) -> int:
    vowels = "aeiou"

    max_ = 0

    # 取出第一個長度為 k 的 subarray 並計算裡面有幾個母音, 當成基礎長度
    sub = 0
    for c in s[0:k]:
        if c in vowels:
            sub += 1

    max_ = sub

    l = len(s)
    i = 1

    # 用 sliding window 的方式跑過每一個單字, 移動的時候只需要判斷
    # 左邊移出來的字母如果是母音的話, 基礎長度 - 1
    # 右邊加進來的字母如果是母音的話, 基礎長度 + 1
    # 再與 max_ 做比較, 回傳最大的 max_
    while i < l - k + 1:
        if s[i - 1] in vowels:
            sub -= 1

        if s[i + (k - 1)] in vowels:
            sub += 1

        max_ = max(max_, sub)

        i += 1

    return max_


if __name__ == "__main__":
    assert max_vowels("abciiidef", 3) == 3
    assert max_vowels("aeiou", 2) == 2
    assert max_vowels("leetcode", 3) == 2
