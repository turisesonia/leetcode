"""
# 238
Medium
Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    result = []
    length = len(nums)

    def prod(ls: list):
        if len(ls) <= 0:
            return 0

        res = ls[0]

        for j in range(1, len(ls)):
            res *= ls[j]

        return res

    for i in range(length):
        left = prod(nums[0:i]) if i > 0 else 1
        right = prod(nums[i + 1 : length]) if i < length - 1 else 1

        result.append(left * right)

    return result


def product_except_self(nums: List[int]) -> List[int]:
    ln = len(nums)

    left_subs = []
    right_subs = []
    ans = [1 for _ in range(ln)]

    for i in range(ln):
        left = left_subs[-1] * nums[i - 1] if i > 0 else 1
        left_subs.append(left)

        right = right_subs[0] * nums[ln - i] if ln - i < ln else 1
        right_subs.insert(0, right)

        ans[i] *= left
        ans[ln - i - 1] *= right

    return ans


def product_except_self(nums: List[int]) -> List[int]:
    """
    解法:
    要取得陣列內自己以外的數相乘的結果, 只要計算每一個元素 "左邊的其他元素相乘" 乘上 "右邊的其他元素相乘" 就是結果
    ex: [1, 2, 3, 4, 5] -> 以 3 為例  左邊為 [1, 2] 1x2 = 2, 右邊為 [4, 5] 4x5 = 20, 答案為 2 x 20 = 40
    """
    # 取得 nums 長度
    ln = len(nums)

    # 當 i = 0 時, 左邊沒有任何元素, 所以用 1 來當初始值, 因 1 * 任何數都不會變
    prev = 1

    # 當 i = len(nums) - 1 即 i 到了最後一個元素, 他的右邊不會再有其他數值了
    post = 1

    # 產生解答用的 ans array
    ans = [1 for _ in range(ln)]

    for i in range(ln):
        ans[i] *= prev
        prev *= nums[i]

        ans[ln - i - 1] *= post
        post *= nums[ln - i - 1]

    return ans


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
