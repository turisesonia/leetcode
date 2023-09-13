"""
# 113
Medium
Path Sum II

https://leetcode.com/problems/path-sum-ii/description/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from typing import Optional
from data_structure.tree import TreeNode


def path_sum(root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
    if not root:
        return []

    res = []
    stack = [(root, [])]

    while stack:
        node, paths = stack.pop()

        paths = paths + [node.val]

        if node.right:
            stack.append((node.right, paths))

        if node.left:
            stack.append((node.left, paths))

        if not node.left and not node.right and sum(paths) == targetSum:
            res.append(paths)

    return res


if __name__ == "__main__":
    pass
