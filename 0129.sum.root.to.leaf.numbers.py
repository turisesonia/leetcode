"""
# 129
Medium
Sum Root to Leaf Numbers

https://leetcode.com/problems/sum-root-to-leaf-numbers/

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
* The number of nodes in the tree is in the range [1, 1000].
* 0 <= Node.val <= 9
* The depth of the tree will not exceed 10.
"""


from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, "")]

        while stack:
            node, prev = stack.pop()

            next_ = prev + str(node.val)

            if node.right:
                stack.append((node.right, next_))

            if node.left:
                stack.append((node.left, next_))

            if not node.left and not node.right:
                total += int(next_)

        return total


class SolutionRecursion:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._sum_leaf_node(root, "")

    def _sum_leaf_node(self, node: Optional[TreeNode], prev: str) -> int:
        next_ = prev + str(node.val)
        if not node.left and not node.right:
            return int(next_)

        sum_ = 0

        if node.left:
            sum_ += self._sum_leaf_node(node.left, next_)

        if node.right:
            sum_ += self._sum_leaf_node(node.right, next_)

        return sum_


if __name__ == "__main__":
    pass
