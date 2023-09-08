"""
# 1448
Medium
Count Good Nodes in Binary Tree

https://leetcode.com/problems/count-good-nodes-in-binary-tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

from data_structure.tree import TreeNode


# def good_nodes(root: TreeNode) -> int:
#     if not root:
#         return 0

#     count = 0
#     stack = [(root, (root.val))]

#     while stack:
#         n, parents = stack.pop()

#         if max(parents) <= n.val:
#             count += 1

#         parents = parents + (n.val)

#         if n.right:
#             stack.append((n.right, parents))

#         if n.left:
#             stack.append((n.left, parents))

#     return count


def good_nodes(root: TreeNode) -> int:
    """
    Solved using DFS (stack ver.)
    """

    if not root:
        return 0

    count = 0
    stack = [(root, root.val)]

    while stack:
        n, max_ = stack.pop()

        if n.val >= max_:
            count += 1

        max_ = max(n.val, max_)

        if n.right:
            stack.append((n.right, max_))

        if n.left:
            stack.append((n.left, max_))

    return count


def good_nodes(root: TreeNode) -> int:
    """
    Solved using DFS (recursive ver.)
    """

    def find(node: TreeNode, maximum: int):
        if not node:
            return 0

        count = 0

        if node.val >= maximum:
            count += 1

        maximum = max(node.val, maximum)

        count += find(node.left, maximum)
        count += find(node.right, maximum)

        return count

    return find(root, root.val)


if __name__ == "__main__":
    pass
