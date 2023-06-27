"""
# 66
Plus one

https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
from typing import List

# v1 answer
# def plus_one(digits: List[int]):
#     plus = 1
#     res = []
#     for i in range(len(digits) - 1, -1, -1):
#         digits[i] += plus

#         if digits[i] < 10:
#             plus = 0

#         res.insert(0, digits[i] % 10)

#     if plus != 0:
#         res.insert(0, 1)

#     return res


# v2 answer
def plus_one(digits: List[int]):
    plus = 1
    last = len(digits) - 1

    if digits[last] < 9:
        digits[last] += 1
        return digits

    while last >= 0:
        digits[last] += plus
        if digits[last] < 10:
            plus = 0
            break
        digits[last] = digits[last] % 10
        last -= 1

    if plus != 0:
        digits.insert(0, 1)

    return digits


if __name__ == "__main__":
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
    assert plus_one([9]) == [1, 0]
