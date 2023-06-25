"""
# 2
Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


class ListNode:
    def __repr__(self):
        ret = f"{self.val}"

        nex = self.next
        while nex is not None:
            ret += f" -> {nex.val}"
            nex = nex.next

        return ret

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def list_to_linked(ls: list):
    if len(ls) == 1:
        return ListNode(ls[0])

    return ListNode(ls[0], list_to_linked(ls[1:]))


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    first = ListNode(l1.val + l2.val)

    print(first)

if __name__ == "__main__":
    l1 = list_to_linked([2, 4, 3])
    l2 = list_to_linked([5, 6, 4])

    add_two_numbers(l1, l2)
