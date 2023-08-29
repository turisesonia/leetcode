"""
# 100
Easy
Same Tree

https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
"""

from typing import Optional
from data_structure.tree import TreeNode, list_to_binary_tree


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    pq = [p]
    plist = []

    qq = [q]
    qlist = []

    while len(pq) > 0:
        node = pq.pop(0)
        if node:
            plist.append(node.val)

            pq.append(node.left)
            pq.append(node.right)
        else:
            plist.append(None)

    while len(qq) > 0:
        node = qq.pop(0)
        if node:
            qlist.append(node.val)

            qq.append(node.left)
            qq.append(node.right)
        else:
            qlist.append(None)

    return plist == qlist


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Recursion
    """

    def is_same(p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None and q is None:
            # Is the same node when both nodes are equal to NULL
            return True
        elif p is None or q is None:
            # Is different node when only one node equal to NULL
            return False
        elif p.val != q.val:
            # Is different node when both values are different
            return False

        # check the left node and the right node baseed on both parent nodes.
        return is_same(p.left, q.left) and is_same(p.right, q.right)

    return is_same(p, q)


if __name__ == "__main__":
    p = list_to_binary_tree([1, 2, 3])
    q = list_to_binary_tree([1, 2, 3])

    assert is_same_tree(p, q)

    p = list_to_binary_tree([1, 2])
    q = list_to_binary_tree([1, None, 2])

    assert not is_same_tree(p, q)

    p = list_to_binary_tree([1, 2, 1])
    q = list_to_binary_tree([1, 1, 2])

    assert not is_same_tree(p, q)
