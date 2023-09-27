"""
# 437
Medium
Path Sum III

https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Record the sum of prefix paths before the current node
        # Set key:value = 0:1 to represent that the root node's value is equal to targetSum
        hm = {0: 1}

        # the number of path sum equals to targetSum
        self.ans = 0

        def dfs(node: Optional[TreeNode], prev_sum: int):
            if not node:
                return

            # get the paths sum from root node to current node
            path_sum = prev_sum + node.val

            # 如果 path_sum 減去 targerSum 的值有出現在先前紀錄的 hm (prefix paths sum) 內
            # 代表此路徑是要找的答案
            needed = path_sum - targetSum
            self.ans += hm.get(needed, 0)

            # 將現在的路徑和記錄起來
            hm[path_sum] = hm.get(path_sum, 0) + 1

            # 繼續往下找
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

            # ! 這段 node 以下的路徑已經都全部找完了，扣掉 1 以免別的路徑有相同的 preifx sum
            hm[path_sum] -= 1

        dfs(root, 0)

        return self.ans


if __name__ == "__main__":
    pass
