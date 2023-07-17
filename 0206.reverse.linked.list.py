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
    """
    把 Linked node 每個元素都跑一遍並存至 list 內
    用堆疊的方式再將 list 內元素取出來並產生反轉後的 linked list

    O(2n)
    """
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
    """
    prev    上一次所在的 node
    current 現在所在的 node

    每次執行時, 將現在所在的 node 的 val 產生出新的一個 ListNode, 並把 next 指到 prev
    完成後 current 往前一個位置直到沒有下一個 (current = current.next)
    """
    prev, current = None, head

    while current is not None:
        val = current.val

        if not prev:
            prev = ListNode(val)
        else:
            prev = ListNode(val, prev)

        current = current.next

    return prev


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    prev    上一次所在的 node
    current 現在所在的 node

    處理流程:
    先將 current.next 的 node 暫存到 temp 變數
    temp = current.next ("2" ->3->4->5)

    接下來把 current.next 指向 prev (如果是第一次即指向 None)
    current.next = prev  ("1" -> None)

    完成後, 將現在的 current 放到 prev (prev = current)
    prev = current

    current 繼續向前移動 (current = temp)
    current = temp
    """
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4, 5])
    reverse = reverse_list(head)
    assert linked_to_list(reverse) == [5, 4, 3, 2, 1]

    head = list_to_linked([1, 2])
    reverse = reverse_list(head)
    assert linked_to_list(reverse) == [2, 1]
