"""
# 103
Medium
Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

from typing import Optional, List
from data_structure.tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        orders = []

        queue = [(root, 1, True)]

        while queue:
            node, lv, direction = queue.pop(0)

            if lv > len(orders):
                orders.append([])

            idx = lv - 1

            if direction:
                orders[idx].append(node.val)
            else:
                orders[idx].insert(0, node.val)

            if node.left:
                queue.append((node.left, lv + 1, not direction))

            if node.right:
                queue.append((node.right, lv + 1, not direction))

        return orders
