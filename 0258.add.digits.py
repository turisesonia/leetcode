"""
# 258
Add Digits
Easy

https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

找到規則, 下列每一排的每個位數相加剛好是 1 ~ 9
1, 2, 3, 4, 5, 6, 7, 8, 9

10, 11, 12, 13, 14, 15, 16, 17, 18

19, 20, 21, 22, 23, 24, 25, 26, 27

19 -> 1+9 -> 10 -> 1+0 = 1

所以可看出每 9 個數字是一個循環, 只要找到 num 的餘數就是代表他的位數和至個位數
但是要處理例外, 當 num 剛好整除 9 時, 此時的位數和至個位數會是 9
"""


def add_digits(num: int) -> int:
    if num == 0:
        return 0

    remain = num % 9

    return remain if remain else 9


if __name__ == "__main__":
    assert add_digits(38) == 2
    assert add_digits(1278) == 9
    assert add_digits(0) == 0
