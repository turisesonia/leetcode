"""
# 1161
Medium
Maximum Level Sum of a Binary Tree

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


Example 1:

https://assets.leetcode.com/uploads/2019/05/03/capture.JPG

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """BFS

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            List[int]: _description_
        """
        min_lv = 1

        if not root:
            return min_lv

        # 記錄層數
        prev_lv = 1
        # 記錄上一層總和
        prev_sum = 0
        # 宣告 -inf 為初始的最小值
        max_ = float("-inf")

        queue = [(root, prev_lv)]

        while queue:
            node, lv = queue.pop(0)

            if lv > prev_lv:
                if prev_sum > max_:
                    max_ = prev_sum
                    min_lv = prev_lv
                prev_lv = lv
                prev_sum = 0

            # 每探訪 node 時加總 prev_sum
            prev_sum += node.val

            if node.left:
                queue.append((node.left, lv + 1))

            if node.right:
                queue.append((node.right, lv + 1))

        if prev_sum > max_:
            min_lv = prev_lv

        return min_lv
