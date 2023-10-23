"""
# 501
Easy
Find Mode in Binary Search Tree

https://leetcode.com/problems/find-mode-in-binary-search-tree/

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""

from typing import Optional, List
from data_structure.tree import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.hm = {}
        self.dfs(root)

        ans = []
        prev = float("-inf")
        for val, count in self.hm.items():
            if count > prev:
                ans = [val]
                prev = count

            elif count == prev:
                ans.append(val)

        return ans

    def dfs(self, node: Optional[TreeNode]):
        val = node.val

        self.hm[val] = self.hm.get(val, 0) + 1

        if node.left:
            self.dfs(node.left)

        if node.right:
            self.dfs(node.right)
