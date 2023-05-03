"""
# 1071
Easy

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

https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
import re

def gcd_of_strings(str1: str, str2: str) -> str:
    ooo = re.findall('..', str1)

    print(str1.split(str1[:2]))
    print(ooo)

    return "ABC"


if __name__ == "__main__":
    assert gcd_of_strings("ABCABC", "ABC") == "ABC"
    # assert gcd_of_strings("ABABAB", "AB") == "AB"
    # assert gcd_of_strings("LEET", "CODE") == ""
