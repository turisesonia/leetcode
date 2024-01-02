"""
# 138
Medium
Copy List with Random Pointer

https://leetcode.com/problems/copy-list-with-random-pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list.
The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
* val: an integer representing Node.val
* random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
https://assets.leetcode.com/uploads/2019/12/18/e1.png

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
https://assets.leetcode.com/uploads/2019/12/18/e2.png

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
https://assets.leetcode.com/uploads/2019/12/18/e3.png

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
* 0 <= n <= 1000
* -10^4 <= Node.val <= 10^4
* Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    利用一個額外的 Hash map 來記錄原本的 node 對應到複製出來的 node

    Ex:
    # Original Linked List
    7 -> 13 -> 11 -> 10 -> 1

    # Copied Linked List
    7' -> 13' -> 11' -> 10' -> 1'

    Hash map
    {
        7: 7',
        13: 13',
        11: 11',
        10: 10',
        1: 1'
    }
    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        hm = {None: None}
        current = head

        # copied node
        new_head = Node(x=0)
        nc = new_head
        prev = None

        while current:
            nc.val = current.val

            if current.next:
                nc.next = Node(x=0)

            if prev is not None:
                prev.next = nc

            hm[current] = nc

            current = current.next
            prev = nc
            nc = nc.next

        while head:
            node = hm[head]
            node.random = hm[head.random]

            head = head.next

        return new_head


from collections import defaultdict


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        hm = defaultdict(lambda: Node(0))
        hm[None] = None

        current = head

        while current:
            node = hm[current]
            node.val = current.val
            node.next = hm[current.next]
            node.random = hm[current.random]

            current = current.next

        return hm[head]


if __name__ == "__main__":
    pass
