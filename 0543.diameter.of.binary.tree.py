"""
# 543
Easy
Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:

https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
- The number of nodes in the tree is in the range [1, 104].
- -100 <= Node.val <= 100
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        BFS then DFS
        """
        if not root:
            return 0

        max_ = 0
        queue = [root]

        while queue:
            n = queue.pop(0)

            left = self.dfs(n.left)
            right = self.dfs(n.right)

            if n.left:
                queue.append(n.left)

            if n.right:
                queue.append(n.right)

            max_ = max(max_, left + right)

        return max_

    def dfs(self, node: Optional[TreeNode]):
        max_ = 0

        if not node:
            return max_

        stack = [(node, 1)]
        while stack:
            n, depth = stack.pop()

            if n and n.right:
                stack.append((n.right, depth + 1))

            if n and n.left:
                stack.append((n.left, depth + 1))

            max_ = max(max_, depth)

        return max_


# Solution from leetcode 需再次複習理解
class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)

        return self.max

    def height(self, node: Optional[TreeNode]):
        left = self.height(node.left) if node.left else 0
        right = self.height(node.right) if node.right else 0

        self.max = max(self.max, left + right)

        return 1 + max(left, right)


if __name__ == "__main__":
    pass
