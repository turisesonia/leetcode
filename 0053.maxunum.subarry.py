"""
# 53
Medium

https://leetcode.com/problems/maximum-subarray/

Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

使用 Kadane's Algorithm 解
演算法解釋:
如果已知 nums[:i] 的最大總和, 那麼 nums[:i+1] 的最大總和必定 "包含" 或 "不包含" nums[:i] 的 Prefix.

Ex:
# 傳入的 list
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 用來儲存每個 index 位置時最大的 subarray sum 的值
store = []

# 來處理是否包含 nums[:i] 的 prefix
max_end_num

- idx = 0
直接放入 store 內, 一定是當下最大的 sub array sum (因為只有一個元素)

- idx = 1 ~ n
取出 store 內的最後一個元素 prefix_num, 代表演算法中的 Prefix
有兩種狀況

1. prefix_num < 0
代表之前的最大總和是負的, 即 nums[:i+1] "不包含" prefix_num
max_end_num = 0
store.append(nums[idx] + max_end_num)

2. prefix_num >= 0, 即 nums[:i+1] "包含" prefix_num
max_end_num = prefix_num
store.append(nums[idx] + max_end_num)

最後回傳 store 最大的值就是解答
return max(store)
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    # store
    store = [nums[0]]

    for n in nums[1:]:
        max_end = store[-1] if store[-1] > 0 else 0

        max_sum = n + max_end

        store.append(max_sum)

    return max(store)


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1]) == -1
    assert max_sub_array([-2, 1]) == 1
    assert max_sub_array([-2, -1]) == -1
