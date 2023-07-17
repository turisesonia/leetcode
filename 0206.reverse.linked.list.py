"""
# 206
Easy
Reverse Linked List

https://leetcode.com/problems/reverse-linked-list

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked, linked_to_list


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    stack = [head.val]

    ln = head.next
    while ln is not None:
        stack.append(ln.val)
        ln = ln.next

    root = ListNode(stack.pop())
    current = root

    for i in range(len(stack) - 1, -1, -1):
        current.next = ListNode(stack[i])
        current = current.next

    return root


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    current = head
    while current is not None:
        val = current.val

        if not prev:
            prev = ListNode(val)
        else:
            prev = ListNode(val, prev)

        current = current.next

    return prev


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    pre = None

    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4, 5])
    reverse = reverse_list(head)
    assert linked_to_list(reverse) == [5, 4, 3, 2, 1]

    head = list_to_linked([1, 2])
    reverse = reverse_list(head)
    assert linked_to_list(reverse) == [2, 1]
