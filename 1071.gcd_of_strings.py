"""
# 1071
Easy

https://leetcode.com/problems/greatest-common-divisor-of-strings/

Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

HINT
If you're stuck on this and need a hint, there are a few observations that may be helpful:

1. Since the candidate string needs to evenly divide str1 and str2 we only need to consider candidate strings with a length that is evenly divisible into the length of both str1 and str2. This quickly provides us with a solution that significantly outperforms brute-force.

2. As a result of the above, we only need to try string lengths up to the length of the shorter of our two input strings. This gives us our bounds for determining candidate string lengths.

3. Since we are looking for the longest candidate we can begin our iteration from the largest string length that evenly divides both strings and work downward to smaller length strings. The first string that fits our criteria is then our answer.
"""


def gcd_of_strings(str1: str, str2: str) -> str:
    x, y = len(str1), len(str2)

    if y > x:
        str1, str2 = str2, str1
        x, y = y, x

    l = x

    while y > 0:
        x, y = y, x % y

    step = l // x

    while step > 0:
        sub = str2[:x]
        if sub * (len(str2) // x) == str2 and sub * step == str1:
            return sub

        step -= 1

    return ""


if __name__ == "__main__":
    assert gcd_of_strings("ABCABC", "ABC") == "ABC"
    assert gcd_of_strings("ABABAB", "AB") == "AB"
    assert gcd_of_strings("ABABAB", "ABAB") == "AB"
    assert gcd_of_strings("ABABAB", "ABD") == ""
    assert gcd_of_strings("LEET", "CODE") == ""
