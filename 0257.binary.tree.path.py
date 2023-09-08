"""
# 257
Easy
Binary Tree Paths

https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""


from typing import Optional
from data_structure.tree import TreeNode


def binary_tree_paths(root: Optional[TreeNode]) -> list[str]:
    """
    Solved using DFS
    """

    paths = []

    if root:
        stack = [(root, "")]

        while stack:
            n, parent = stack.pop()

            if not n.left and not n.right:
                paths.append(f"{parent}{n.val}")

            parent = parent + f"{n.val}->"

            if n.right:
                stack.append((n.right, parent))

            if n.left:
                stack.append((n.left, parent))

    return paths


if __name__ == "__main__":
    pass
