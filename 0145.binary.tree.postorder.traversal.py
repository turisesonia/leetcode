"""
# 145
Easy
Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.


後序 (postorder): left -> right -> root (From deep to top)

    1
   / \
  2   3
 / \ / \
4  5 6  7

=> 4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional
from data_structure.tree import TreeNode


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    res = []

    if not root:
        return res

    stack = [root]

    while stack:
        n = stack.pop()

        # res.append(n.val)
        res.insert(0, n.val)

        if n.left:
            stack.append(n.left)

        if n.right:
            stack.append(n.right)

    return res


if __name__ == "__main__":
    pass
