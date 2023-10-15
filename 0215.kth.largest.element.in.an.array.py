"""
# 215
Medium
Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = [None]
        self.length = 0

        for num in nums:
            self.insert(num)

        for _ in range(k):
            ans = self.extract()
            print(ans)

        return ans

    def insert(self, num: int):
        self.heap.append(num)
        self.length += 1

        k = self.length
        # up check
        while k > 1 and self.heap[k] > self.heap[k // 2]:
            self._exchange(k, k // 2)
            k //= 2

    def extract(self):
        self._exchange(1, -1)
        max_ = self.heap.pop()
        self.length -= 1

        # down chek
        idx = 1
        while 2 * idx <= self.length:
            i = 2 * idx

            k = i
            if i < self.length and self.heap[i + 1] > self.heap[i]:
                k = i + 1

            if self.heap[k] > self.heap[idx]:
                self._exchange(idx, k)

            idx = k

        return max_

    def _exchange(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


if __name__ == "__main__":
    solu = Solution()
    assert solu.findKthLargest([3, 2, 1, 5, 6, 4], k=2) == 5
    assert solu.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
