"""
# 637
Easy
Average of Levels in Binary Tree

https://leetcode.com/problems/average-of-levels-in-binary-tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^-5 of the actual answer will be accepted.

Example 1:

https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
* The number of nodes in the tree is in the range [1, 104].
* -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional, List
from data_structure.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        hm = {0: 0}
        result = []
        queue = [(0, root)]

        while queue:
            lv, node = queue.pop(0)

            if lv not in hm:
                result[lv - 1] /= hm[lv - 1]
                hm[lv] = 0

            if len(result) < lv + 1:
                result.append(0)

            result[lv] += node.val
            hm[lv] += 1

            if node.left:
                queue.append((lv + 1, node.left))

            if node.right:
                queue.append((lv + 1, node.right))

        result[lv] /= hm[lv]

        return result


if __name__ == "__main__":
    pass
