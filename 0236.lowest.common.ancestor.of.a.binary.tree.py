"""
# 236
Medium
Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

https://assets.leetcode.com/uploads/2018/12/14/binarytree.png

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

https://assets.leetcode.com/uploads/2018/12/14/binarytree.png

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 105].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.
"""

from data_structure.tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # return current node if it's equal to None / p / q
        if root is None or root == p or root == q:
            return root

        # 尋找 p, q 是在左邊還是右邊的 subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # 如果 left, right 均不為 None 代表 p, q 在不同的 subtree, 回傳當下的 root
            return root
        elif left:
            # 代表 p, q 均在左 subtree, 回傳 left
            # 原因為在 45 行的 if-else 時，如果找到 root == p or root == q 就會停止 left 尋找
            # 接下來在如果 right 沒找到一定在 left 底下
            return left
        else:
            # 代表 p, q 均在右 subtree, 回傳 right
            return right


if __name__ == "__main__":
    pass
