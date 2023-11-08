"""
# 19
Medium
Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    1. 完整跑一遍 linked list 後將所有 node 存進 list 內
    2. 將指定位置的前後 node 連起來
    """

    items = []
    current = head

    while current:
        items.append(current)
        current = current.next

    total = len(items)
    pos = total - n

    if pos == 0:
        head = head.next
    elif pos == total - 1:
        items[pos - 1].next = None
    else:
        items[pos - 1].next = items[pos].next

    return head


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    1. 利用快慢指針來找到要移除的 node
    2. n 的數字就是快慢指針的 node 差距 (ex: n = 2, fast 快 slow 兩個 node)
       先將 fast 往前移動 n 步
    3. 同時一步一步移動 slow, fast 指針
    4. 當 fast 移動到最後一個 node 時, 代表 slow 的下一個就是要移除的 node
    """
    if not head or not head.next:
        return None

    dummy = ListNode(-1, head)
    slow, fast = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    node = list_to_linked([1, 2, 3, 4, 5])
    head = remove_nth_from_end(node, 2)
    print("---", head)

    node = list_to_linked([1, 2])
    head = remove_nth_from_end(node, 2)
    print("---", head)

    node = list_to_linked([1, 2])
    head = remove_nth_from_end(node, 1)
    print("---", head)

    node = list_to_linked([1, 2, 3])
    head = remove_nth_from_end(node, 2)
    print("---", head)
