"""
# 2095
Medium
Delete the Middle Node of a Linked List

https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked, linked_to_list


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    完整遍歷 linked list 後, 將所有的 Node 存進 list 內
    1. 取得 list 的中間值 (middle index)
    2. 將中間值前一個 Node 的 next 指向 中間值 Node 的 next (即刪除中間 Node)

    example:
    Linked node: 1 -> 2 -> 3 -> 4 -> 5
    list: [ 1(->2->3->4->5), 2(->3->4->5), 3(->4->5), 4(->5), 5 ]
    last of middle: 2(->3->4->5)
    middle of list: 3(->4->5)

    2.next 指向 3.next
    2->4->5

    head: 1 -> 2 -> 4 -> 5

    time: O(n)
    space: O(n)
    """
    if not head.next:
        return None

    curr = head
    pos = []

    while curr:
        next_ = curr.next

        pos.append(curr)

        curr = next_

    mid = len(pos) // 2
    pos[mid - 1].next = pos[mid].next

    return head


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Slow & Fast Pointer (Hare & Tortoise Algorithm 龜兔演算法)

    宣告兩個指針 slow & fast, fast 指針的移動長度都會是 slow 的兩倍
    所以當 fast 指針移動到最後一個 node 時, slow 就會剛好在 middle node
    """
    if not head.next:
        return None

    prev = head
    slow = head
    fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


if __name__ == "__main__":
    head = list_to_linked([1, 3, 4, 7, 1, 2, 6])
    head = delete_middle(head)
    assert linked_to_list(head) == [1, 3, 4, 1, 2, 6]

    head = list_to_linked([1, 2, 3, 4])
    head = delete_middle(head)
    assert linked_to_list(head) == [1, 2, 4]

    head = list_to_linked([2, 1])
    head = delete_middle(head)
    assert linked_to_list(head) == [2]

    head = list_to_linked([1])
    head = delete_middle(head)
    assert linked_to_list(head) == []
