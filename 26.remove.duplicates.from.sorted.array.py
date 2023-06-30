"""
# 26
Remove Duplicates from Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

# ! 此題在 nums 傳入是用 reference 的方式, Leetcode 網站在驗證時會驗證此 list 的內容, 所以在解題時必須直接處理 nums 裡的元素.
# ! 且題目要的答案只要 nums 內的 "唯一" 值不重複的排在最前面即可, 並不關心剩下的結果
# ! 解成這樣就可以了: [1,1,2,2,3,3,4,4,4,5,5,5,5,5,5] => [1,2,3,4,5,3,4,4,4,5,5,5,5,5,5]
"""
from typing import List


# v1 每個元素都會跑, 速度較慢
def remove_duplicates(nums: List[int]) -> int:
    tmp = []
    count = 0

    for idx in range(len(nums)):
        n = nums[idx - count]

        if n in tmp:
            nums.pop(idx - count)
            count += 1
            continue

        tmp.append(n)

    return len(nums)


# v2 python 專用解法, 直接找出不重複的元素, 並修改前面幾個不重複元素的數量
def remove_duplicates(nums: List[int]) -> int:
    uniq = list(set(nums))
    uniq.sort()

    for idx, n in enumerate(uniq):
        nums[idx] = n

    return len(uniq)


if __name__ == "__main__":
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_duplicates([1, 1]) == 1
    assert remove_duplicates([1, 1, 1, 1]) == 1
    assert remove_duplicates([-1, 0, 0, 0, 0, 3, 3]) == 3
