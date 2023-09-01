"""
# 108
Easy
Convert Sorted Array to Binary Search Tree

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, convert it to a `height-balanced` binary search tree.

Height Balanced:
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.

Reference
https://medium.com/confessions-of-a-bootcamp-grad/how-to-solve-leetcodes-convert-sorted-array-to-binary-search-tree-problem-with-javascript-a61e6d6d6c36
"""

from typing import Optional
from data_structure.tree import TreeNode, list_to_binary_tree, binary_tree_to_list


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    def middle(nums: list[int]):
        if len(nums) <= 0:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = middle(nums[0:mid])
        node.right = middle(nums[mid + 1 :])

        return node

    return middle(nums)


if __name__ == "__main__":
    # output [0, -3, 9, -10, null, 5]
    root = sorted_array_to_bst([-10, -3, 0, 5, 9])

    # output [3, 1]
    root = sorted_array_to_bst([1, 3])

    # output [3, 1, 5, 0, 2, 4]
    root = sorted_array_to_bst([0, 1, 2, 3, 4, 5])
