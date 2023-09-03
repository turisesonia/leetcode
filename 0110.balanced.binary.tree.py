"""
# 110
Easy
Balanced Binary Tree

https://leetcode.com/problems/balanced-binary-tree/?envType=daily-question&envId=2023-09-01

Given a binary tree, determine if it is height-balanced.

** height-balanced **
Every node's left sub-tree and right sub-tree differ not more than one

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""

from typing import Optional
from data_structure.tree import TreeNode, list_to_binary_tree


def is_balanced(root: Optional[TreeNode]) -> bool:
    def depth(root: TreeNode):
        if not root:
            return 0

        left_depth = depth(root.left)
        if left_depth < 0:
            return -1

        right_depth = depth(root.right)
        if right_depth < 0 or abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    return depth(root) >= 0


if __name__ == "__main__":
    root = list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    assert is_balanced(root)

    root = list_to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert not is_balanced(root)

    assert is_balanced(None)

    root = list_to_binary_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    assert not is_balanced(root)
