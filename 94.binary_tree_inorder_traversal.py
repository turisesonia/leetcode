"""
# 94
Easy
Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import Optional, List
from data_structure.binary_tree import Node


def inorder_traversal(root: Optional[Node]) -> List[int]:
    ls = []

    _traversal(root, ls)

    return ls


def _traversal(current: Node, ls: list):
    if not current:
        return

    # in order traversal, left -> root -> right
    if current.left:
        _traversal(current.left, ls)

    ls.append(current.val)

    if current.right:
        _traversal(current.right, ls)


if __name__ == "__main__":
    inorder_traversal()