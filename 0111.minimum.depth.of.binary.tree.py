"""
# 111
Easy
Minimum Depth of Binary Tree

https://leetcode.com/problems/minimum-depth-of-binary-tree/?envType=daily-question&envId=2023-09-04

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000
"""

from typing import Optional
from data_structure.tree import TreeNode


def min_depth(root: Optional[TreeNode]) -> int:
    def minimum(node: Optional[TreeNode]):
        if not node:
            return 0

        elif not node.left:
            return 1 + minimum(node.right)

        elif not node.right:
            return 1 + minimum(node.left)

        else:
            return 1 + min(minimum(node.left), minimum(node.right))

    return minimum(root)


def min_depth(root: Optional[TreeNode]) -> int:
    """
    Solved using queue solution.

    Find the first leaf node, it's minimum depth in this tree.
    """
    if not root:
        return 0

    items = [(root, 1)]

    while len(items) > 0:
        n, depth = items.pop(0)

        if n.left:
            items.append((n.left, depth + 1))

        if n.right:
            items.append((n.right, depth + 1))

        if not n.left and not n.right:
            return depth


if __name__ == "__main__":
    pass
    # root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    # assert min_depth(root) == 2

    # root = list_to_binary_tree([2, None, 3, None, 4, None, 5, None, 6])
    # assert min_depth(root) == 5
