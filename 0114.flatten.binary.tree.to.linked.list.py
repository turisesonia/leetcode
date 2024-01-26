"""
# 114
Medium
Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list

Given the root of a binary tree, flatten the tree into a "linked list":

* The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
* The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:

https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]


Constraints:
* The number of nodes in the tree is in the range [0, 2000].
* -100 <= Node.val <= 100

Follow up:
Can you flatten the tree in-place (with O(1) extra space)?
"""

from typing import Optional
from data_structure.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        Not O(1) extra space
        """
        if not root:
            return

        current = None
        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            if not current:
                current = node
                current.left = None
            else:
                node.left = None
                current.right = node
                current = current.right


if __name__ == "__main__":
    pass