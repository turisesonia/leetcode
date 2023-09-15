"""
# 437
Medium
Path Sum III

https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

from typing import Optional
from data_structure.tree import TreeNode


def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
    if not root:
        return 0

    count = 0
    stack = [(root, 0)]

    while stack:
        node, prev = stack.pop()

        sum_ = prev + node.val

        if sum_ == targetSum:
            count += 1
            prev = 0
        elif sum_ > targetSum:
            prev = 0
        else:
            prev = sum_

        if node.right:
            stack.append((node.right, prev))

        if node.left:
            stack.append((node.left, prev))

    return count


if __name__ == "__main__":
    pass
