"""
# 83
Easy
Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked, linked_to_list


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    沒注意到題目是 sorted linked list, 其實不需要 duplicates
    """
    current = head
    prev = None
    duplicate = []

    while current:
        val = current.val

        if val not in duplicate:
            duplicate.append(val)
            prev = current
        else:
            prev.next = current.next

        current = current.next

    return head


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    prev = head
    current = head.next

    while current:
        if current.val == prev.val:
            prev.next = current.next
        else:
            prev = current

        current = current.next

    return head


if __name__ == "__main__":
    head = list_to_linked([1, 1, 2])
    head = delete_duplicates(head)
    assert linked_to_list(head) == [1, 2]

    head = list_to_linked([1, 1, 2, 3, 3])
    head = delete_duplicates(head)
    assert linked_to_list(head) == [1, 2, 3]

    head = list_to_linked([1, 1, 1])
    head = delete_duplicates(head)
    assert linked_to_list(head) == [1]
