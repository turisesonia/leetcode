"""
# 404
Easy
Sum of Left Leaves

https://leetcode.com/problems/sum-of-left-leaves/

Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children.
A left leaf is a leaf that is the left child of another node.


Example 1:

https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0


Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

from typing import Optional
from data_structure.tree import TreeNode


def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
    """
    Solved using DFS
    """
    if not root:
        return 0

    sum_ = 0
    stack = [root]

    while stack:
        n = stack.pop()

        if n.right:
            stack.append(n.right)

        left = n.left
        if left:
            if not left.left and not left.right:
                sum_ += left.val
            else:
                stack.append(left)

    return sum_


if __name__ == "__main__":
    pass
