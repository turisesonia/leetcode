"""
# 328
Medium
Odd Even Linked List

https://leetcode.com/problems/odd-even-linked-list

Given the head of a singly linked list,
給定 head 的為一個單鏈的 linked list

group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
將所有奇數索引的節點群組在一起, 接著將偶數索引的節點群組再一起, 回傳重新排序後的 linked list

The first node is considered odd, and the second node is even, and so on.
第一個節點的索引是奇數, 而接著第二個就是偶數 以此類推

Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked, linked_to_list


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return head

    i = 1
    odd, even = None, None
    prev = None
    current = head

    while current:
        if i % 2:
            pass
        else:
            pass

        i += 1
        current = current.next

    print(odd, even)

    return head


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4, 5])
    result = odd_even_list(head)

    assert linked_to_list(result) == [1, 3, 5, 2, 4]

    head = list_to_linked([2, 1, 3, 5, 6, 4, 7])
    result = odd_even_list(head)

    assert linked_to_list(result) == [2, 3, 6, 7, 1, 5, 4]
