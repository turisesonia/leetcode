"""
# 107
Medium
Binary Tree Level Order Traversal II

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Example 1:

https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

from typing import Optional, List
from data_structure.tree import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        orders = []

        queue = [(root, -1)]

        while queue:
            node, lv = queue.pop(0)

            if abs(lv) > len(orders):
                orders.insert(0, [])

            orders[lv].append(node.val)

            if node.left:
                queue.append((node.left, lv - 1))

            if node.right:
                queue.append((node.right, lv - 1))

        return orders