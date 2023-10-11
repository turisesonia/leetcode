"""
# 450
Medium
Delete Node in a BST

https://leetcode.com/problems/delete-node-in-a-bst

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.


Example 1:

https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg
https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105

Follow up:
Could you solve it with time complexity O(height of tree)?
"""


from typing import Optional
from data_structure.tree import TreeNode


class SolutionFromLeetCode:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # search for the value in left sub-tree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        # search for the value in right sub-tree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            # either no child or only one child
            if root.left is None or root.right is None:
                root = root.left if root.left else root.right

            # two child
            else:
                # * Find the inorder successor node
                curr = root.right
                while curr.left:
                    curr = curr.left

                # * Replace inorder successor node val to deleted val
                root.val = curr.val
                # * 往下刪除此 inorder successor node
                root.right = self.deleteNode(root.right, curr.val)

        return root
