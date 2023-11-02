"""
# 12
Medium
Integer to Roman

https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example,
2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
"""


def int_to_roman(num: int) -> str:
    symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    number_of_digit = 1

    output = ""

    while num:
        digit = 10 ** (number_of_digit - 1)

        mod = num % 10

        if mod > 0:
            if mod > 5:
                count = mod - 5

                if count == 4:
                    string = symbols[digit] + symbols[10 * digit]
                else:
                    string = symbols[5 * digit] + symbols[digit] * count

                output = string + output

            elif mod < 5:
                if mod == 4:
                    string = symbols[digit] + symbols[5 * digit]
                else:
                    string = symbols[digit] * mod

                output = string + output
            else:
                output = symbols[mod * digit] + output

        num //= 10
        number_of_digit += 1

    return output


if __name__ == "__main__":
    assert int_to_roman(3) == "III"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(1994) == "MCMXCIV"
