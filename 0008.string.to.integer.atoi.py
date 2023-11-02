"""
# 8
Medium
String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/description/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.


Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


# 直覺解  較慢
def my_atoi(s: str) -> int:
    max_ = 2**31 - 1
    min_ = -(2**31)
    pos_or_neg = None

    num = ""

    for char in s.strip():
        if len(num) == 0 and not pos_or_neg:
            if char == "-":
                pos_or_neg = -1

            elif char == "+":
                pos_or_neg = 1

            elif char.isnumeric():
                pos_or_neg = 1
                num += char
            else:
                break

            continue

        if char.isnumeric():
            num += char
        else:
            break

    res = int(num) * pos_or_neg if len(num) > 0 else 0

    if res > max_:
        res = max_

    if res < min_:
        res = min_

    return res


def my_atoi(s: str) -> int:
    if not s:
        return 0

    max_ = 2**31 - 1
    min_ = -(2**31)
    postive = True

    # pointer index and end of string index
    p, end = 0, len(s)

    # handle leading white space
    while p < end and s[p] == " ":
        p += 1

    if p >= end:
        return 0

    # handle postive or negiteve
    if s[p] == "+" or s[p] == "-":
        postive = s[p] == "+"
        p += 1

    num = 0
    while p < end and s[p].isdigit():
        # 每經過一個數字十進位一次
        num *= 10
        num += int(s[p])

        p += 1

    num *= 1 if postive else -1

    if num > max_:
        num = max_

    if num < min_:
        num = min_

    return num


if __name__ == "__main__":
    assert my_atoi("42") == 42
    assert my_atoi("   -42") == -42
    assert my_atoi("4193 with words") == 4193
    assert my_atoi("000004193 with words") == 4193
    assert my_atoi("words and 987") == 0
    assert my_atoi("-91283472332") == -2147483648
    assert my_atoi(" ") == 0
