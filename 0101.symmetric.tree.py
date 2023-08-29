"""
# 101
Easy
Symmetric Tree
(Mirror Tree)

https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional
from data_structure.tree import TreeNode, list_to_binary_tree


def is_symmetric(root: Optional[TreeNode]) -> bool:
    left = root.left
    right = root.right

    def is_same(left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False

        return is_same(left.left, right.right) and is_same(left.right, right.left)

    return is_same(left, right)


if __name__ == "__main__":
    root = list_to_binary_tree([1, 2, 2, 3, 4, 4, 3])
    assert is_symmetric(root)

    root = list_to_binary_tree([1, 2, 2, None, 3, None, 3])
    assert not is_symmetric(root)
