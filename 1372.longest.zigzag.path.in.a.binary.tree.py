"""
# 1372
Medium
Longest ZigZag Path in a Binary Tree

https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.



Example 1:
https://assets.leetcode.com/uploads/2020/01/22/sample_1_1702.png

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
https://assets.leetcode.com/uploads/2020/01/22/sample_2_1702.png

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0


Constraints:
The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node: Optional[TreeNode], prev_path_sum: int, pre_dire: str, curr_dire: str):
            """Check every node

            Args:
                node (Optional[TreeNode]):
                prev_path_sum (int): The visited node path sum
                pre_dire (str): Previous node direction
                curr_dire (str): Current node direction
            """
            if not node:
                return

            # Set the path sum of previously visited nodes to zero if visit the same direction twice
            if pre_dire == curr_dire:
                prev_path_sum = 0

            # counting path and check the current path is max path
            path_sum = prev_path_sum + 1
            self.max = max(path_sum, self.max)

            dfs(node.left, path_sum, curr_dire, "left")
            dfs(node.right, path_sum, curr_dire, "right")

        dfs(root.left, 0, None, "left")
        dfs(root.right, 0, None, "right")

        return self.max


if __name__ == "__main__":
    pass
