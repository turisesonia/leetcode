"""
# 226
Easy
Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from typing import Optional
from data_structure.tree import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        node.left, node.right = node.right, node.left

    return root


if __name__ == "__main__":
    pass
