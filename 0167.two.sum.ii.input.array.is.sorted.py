"""
# 167
Medium
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Your solution must use only constant extra space.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
* 2 <= numbers.length <= 3 * 10^4
* -1000 <= numbers[i] <= 1000
* numbers is sorted in non-decreasing order.
* -1000 <= target <= 1000
* The tests are generated such that there is exactly one solution.
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    length = len(numbers)
    for idx, num in enumerate(numbers):
        ans = target - num

        if ans in numbers:
            left, right = idx + 1, length
            while left != right:
                mid = (right + left) // 2

                val = numbers[mid]

                if val > ans:
                    right = mid
                elif val < ans:
                    left = mid
                else:
                    return [idx + 1, mid + 1]


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        left_val = numbers[left]
        right_val = numbers[right]

        sum_ = left_val + right_val
        if sum_ > target:
            right -= 1
        elif sum_ < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == "__main__":
    assert two_sum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert two_sum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert two_sum(numbers=[-1, 0], target=-1) == [1, 2]
    assert two_sum(numbers=[0, 0, 3, 4], target=0) == [1, 2]
    assert two_sum(numbers=[3, 24, 50, 79, 88, 150, 345], target=200) == [3, 6]
