"""
# 415
Easy
Add Strings

https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

Limit:
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


def add_strings(num1: str, num2: str) -> str:
    """
    Intuition

    The variable 'carry' is represents the carry-over for the sum of two numbers in num1 and num2.

    1. Get number (n1, n2) from last to beginning one by one both in nums1 and nums2
    2. The variable 't' is represents the addition of two numbers.
    3. Obtain the quotient and remainder by dividing the 't' by 10
    4. The remainder is answer for the current digit. The quotient is set to the variable 'curry' for next digit.

    """
    res = ""
    carry = 0

    if len(num2) > len(num1):
        num1, num2 = num2, num1

    for i in range(1, len(num1) + 1):
        i *= -1

        n1 = int(num1[i])
        n2 = int(num2[i]) if abs(i) < len(num2) + 1 else 0

        t = n1 + n2 + carry
        carry = t // 10

        res = str(t % 10) + res

    if carry > 0:
        res = str(carry) + res

    return res


def add_strings(num1: str, num2: str) -> str:
    res = []
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1

    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0

        sum_ = n1 + n2 + carry

        res.insert(0, str(sum_ % 10))

        carry = sum_ // 10

        i -= 1
        j -= 1

    return "".join(res)


if __name__ == "__main__":
    assert add_strings("11", "123") == "134"
    assert add_strings("456", "77") == "533"
    assert add_strings("0", "0") == "0"
