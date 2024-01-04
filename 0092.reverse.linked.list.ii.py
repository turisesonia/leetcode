"""
# 92
Medium
Reverse Linked List II

https://leetcode.com/problems/reverse-linked-list-ii

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
* The number of nodes in the list is n.
* 1 <= n <= 500
* -500 <= Node.val <= 500
* 1 <= left <= right <= n
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked, linked_to_list


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        current = head
        prev = None

        if left == 1:
            tail = current
            while right > 0:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                right -= 1

            tail.next = temp

            head = prev

        else:
            start = None
            for i in range(1, left):
                if i == left - 1:
                    start = current
                current = current.next

            sub = current
            times = right - left + 1

            while times > 0:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                times -= 1

            if start:
                start.next = prev
                sub.next = current

        return head


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        # use dummy head
        dummy = ListNode(None, head)

        # 找出經過 left 移動後的前一個 node
        skip = dummy
        current = dummy.next

        # if left greater than 1, move current node
        for _ in range(1, left):
            skip = current
            current = current.next

        prev = None
        tail = current
        for _ in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        skip.next = prev
        tail.next = temp

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    # * Test case 1
    head = list_to_linked([1, 2, 3, 4, 5])
    reverse = sol.reverseBetween(head, left=2, right=4)
    assert linked_to_list(reverse) == [1, 4, 3, 2, 5]

    # * Test case 2
    head = list_to_linked([5])
    reverse = sol.reverseBetween(head, left=1, right=1)
    assert linked_to_list(reverse) == [5]

    # * Test case 3
    head = list_to_linked([3, 5])
    reverse = sol.reverseBetween(head, left=1, right=2)
    assert linked_to_list(reverse) == [5, 3]

    # * Test case 4
    head = list_to_linked([3, 5, 7, 9])
    reverse = sol.reverseBetween(head, left=1, right=2)
    assert linked_to_list(reverse) == [5, 3, 7, 9]

    # * Test case 5
    head = list_to_linked([1, 2, 3, 4, 5])
    reverse = sol.reverseBetween(head, left=3, right=4)
    assert linked_to_list(reverse) == [1, 2, 4, 3, 5]
