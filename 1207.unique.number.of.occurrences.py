"""
# 1207
Easy
Unique Number of Occurrences

https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    counter = {}

    for n in arr:
        if n not in counter:
            counter[n] = 1
        else:
            counter[n] += 1

    occurences = counter.values()

    return len(occurences) == len(set(occurences))


if __name__ == "__main__":
    assert unique_occurrences([1, 2, 2, 1, 1, 3])
    assert not unique_occurrences([1, 2])
    assert unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
