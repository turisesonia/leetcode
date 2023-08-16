"""
# 94
Easy
Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

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

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List
from data_structure.binary_tree import Node


# 遞迴解法
def inorder_traversal_recursive(root: Optional[Node]) -> List[int]:
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


# 迭代解法
def inorder_traversal_iter(root: Optional[Node]) -> List[int]:
    """
    中序遍歷的順序為 left -> root -> right
    1. 首先一直往左走直到碰到 null 為止, 並將沿路走過的節點存入 stack (堆疊: 後進先出)
    2. stack 的最後一個元素就是最左邊的節點, 將 value 存入 result
    3. 將 current 指派為 current 的右邊節點
    4. 之後再重複 1 ~ 3 直到 current = None 且 stack 為空
    """

    result = []

    if not root:
        return result

    stack = []
    current = root

    while current or len(stack) > 0:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


if __name__ == "__main__":
    pass
