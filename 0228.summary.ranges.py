"""
# 228
Easy
Summary Ranges

https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
(ex: [0, 3]: 0 -> 3: [0,1,2,3])

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

找出連續的整數並把它們轉換成數字範圍 (0,1,2 = 0->2)
如果數字前後都不連續, 則單存回傳這個數字 (0,1,2,4,6,7 = 0->2, "4", 6->7)
"""


def summary_ranges(nums: list[int]) -> list[str]:
    result = []

    prev = None
    start = None

    for n in nums:
        if prev is None:
            # first time in for loop
            prev = n
            start = n
            continue

        # continuous integer differ by one
        if n - prev > 1:
            # 檢查 n 是否與 prev 連續, 不連續的話就要判斷是一個範圍還是單個數字, 並把結果寫入 result
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}->{prev}")

            # reset start and prev
            start = n
            prev = n
        else:
            prev = n

    # 最後判斷剩下的結果
    if prev and start:
        if start == prev:
            result.append(str(start))
        else:
            result.append(f"{start}->{prev}")

    return result


if __name__ == "__main__":
    assert summary_ranges([]) == []
    assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
