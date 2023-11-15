"""
# 530
Easy
Minimum Absolute Difference in BST

https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

注意：對二元搜尋樹 (Binary Search Tree, BST) 做 Inorder traversal 就是由小到大依序遍歷。

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        對二元搜尋樹 (Binary Search Tree, BST) 做 Inorder Traversal 就是由小到大依序遍歷。

        ex: [4,2,6,1,3] -> [1,2,3,4,6]
        """
        current = root
        min_ = float("inf")
        pre = None
        stack = []

        # Inorder Traversal
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if pre is None:
                pre = current.val
            else:
                min_ = min(current.val - pre, min_)
                pre = current.val

            current = current.right

        return min_
