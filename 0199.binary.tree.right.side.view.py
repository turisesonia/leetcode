"""
# 199
Medium
Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

More clearly question description and test case:

Give the root of the binary tree, return the values of the right most node at each level of the tree from top to bottom.

A useful test case for this problem would be:
Input: root = [1,2,3,null,5,6,null,4]

https://assets.leetcode.com/users/images/cef92daf-88dd-46b5-a329-b179916c6482_1618278364.1240458.png

The output would be: [1,3,6,4]
"""

from typing import Optional, List
from data_structure.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS

        Args:
            root (Optional[TreeNode]): _description_

        Returns:
            List[int]: _description_
        """
        if not root:
            return []

        # right side
        rs = []

        # 記錄層數
        prev_lv = 0
        # 記錄上一個 node 的值
        prev_val = None

        queue = [(root, prev_lv)]

        while queue:
            node, lv = queue.pop(0)

            # 代表層數往下一層移動 將 prev_val 儲存至 rs 中
            if lv > prev_lv:
                rs.append(prev_val)
                prev_lv = lv

            # 每一次探訪 node 時都記錄他的值
            prev_val = node.val

            if node.left:
                queue.append((node.left, lv + 1))

            if node.right:
                queue.append((node.right, lv + 1))

        rs.append(prev_val)

        return rs
