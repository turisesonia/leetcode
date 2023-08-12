"""
# 203
Easy
Remove Linked List Elements

https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked, linked_to_list


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    curr = head
    prev = None

    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else:
                # 如果前一個 node 不存在, 代表第一個 node 就被刪掉了, 將 head 指到 current.next
                head = curr.next

        else:
            prev = curr

        curr = curr.next

    return head


if __name__ == "__main__":
    head = list_to_linked([1, 2, 6, 3, 4, 5, 6])
    assert linked_to_list(remove_elements(head, 6)) == [1, 2, 3, 4, 5]

    head = list_to_linked([])
    assert linked_to_list(remove_elements(head, 1)) == []

    head = list_to_linked([7, 7, 7, 7])
    assert linked_to_list(remove_elements(head, 7)) == []
