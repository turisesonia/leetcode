"""
# 141
Easy
Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
給定一個 linked list, 檢查在這個 linked list 內是否有循環連結

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false

Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Slow & Fast Pointers (Hare & Tortoise Algorithm)
使用兩個不同速度的指針遍歷線性結構（陣列、序列、鏈結串列）
"""

from typing import Optional
from data_structure.linked import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


if __name__ == "__main__":
    pass
