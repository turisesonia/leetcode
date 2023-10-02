"""
# 700
Easy
Search in a Binary Search Tree

https://leetcode.com/problems/search-in-a-binary-search-tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right

        return None
