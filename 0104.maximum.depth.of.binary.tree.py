"""
# 104
Easy
Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""

from typing import Optional
from data_structure.tree import TreeNode, list_to_binary_tree


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Solved using stack solution.
    """
    if not root:
        return 0

    max_ = 1
    items = [(root, 1)]

    while len(items) > 0:
        n, depth = items.pop()

        if n.left:
            items.append((n.left, depth + 1))

        if n.right:
            items.append((n.right, depth + 1))

        max_ = max(max_, depth)

    return max_


# def max_depth(root: Optional[TreeNode]) -> int:
#     """
#     Leetcode solution using recursion
#     """

#     def dfs(node: TreeNode):
#         if not node:
#             return 0

#         elif not node.left:
#             return 1 + dfs(node.right)

#         elif not node.right:
#             return 1 + dfs(node.left)

#         else:
#             return 1 + max(dfs(node.left), dfs(node.right))

#     return dfs(root)


if __name__ == "__main__":
    root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    assert max_depth(root) == 3

    root = list_to_binary_tree([1, None, 2])
    assert max_depth(root) == 2

    root = list_to_binary_tree([1])
    assert max_depth(root) == 1

    root = list_to_binary_tree([1, 2, 3, 4, 5])
    assert max_depth(root) == 3
