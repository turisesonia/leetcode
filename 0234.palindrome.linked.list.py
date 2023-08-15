"""
# 234
Easy
Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked


def is_palindrome(head: Optional[ListNode]) -> bool:
    curr = head
    stack = []

    while curr:
        stack.append(curr.val)
        curr = curr.next

    for i in range(len(stack) // 2):
        if stack[i] != stack[len(stack) - i - 1]:
            return False

    return True


if __name__ == "__main__":
    head = list_to_linked([1, 2, 2, 1])
    assert is_palindrome(head)

    head = list_to_linked([1, 2])
    assert not is_palindrome(head)
