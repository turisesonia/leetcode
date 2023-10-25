"""
# 216
Medium
Combination Sum III

https://leetcode.com/problems/combination-sum-iii

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
1. Only numbers 1 through 9 are used.
2. Each number is used at most once.

Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []

        # 計算 k 個數字的總和若小於 n 代表沒有組合符合規則
        min_ = sum(i for i in range(1, k + 1))
        if min_ > n:
            return self.ans

        for i in range(1, 10):
            self.sum_combination([], i, k - 1, n - i)

        return self.ans

    def sum_combination(self, pre: list, num: int, k: int, remain: int):
        """
        Args:
            pre (list): 上一層計算的結果
            num (int): 該層要計算的數字
            k (int): 記錄第幾層
            remain (int): n - num
        """
        pre.append(num)
        if k == 0:
            # end of recursion
            if remain == 0:
                self.ans.append(pre)
            return

        for j in range(num + 1, 10):
            if j > remain:
                continue

            self.sum_combination(pre.copy(), j, k - 1, remain - j)


if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum3(3, 7) == [[1, 2, 4]]
    assert sol.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert sol.combinationSum3(4, 1) == []
