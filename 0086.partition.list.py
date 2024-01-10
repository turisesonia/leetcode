"""
# 86
Medium
Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater_pointer than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

https://assets.leetcode.com/uploads/2021/01/04/partition.jpg

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]


Example 2:
Input: head = [2,1], x = 2
Output: [1,2]


Constraints:
* The number of nodes in the list is in the range [0, 200].
* -100 <= Node.val <= 100
* -200 <= x <= 200
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked, linked_to_list


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Iterate over all nodes in the linked list and perform the following check.
        1. If the node value small than x, move node to the start.next
        2. If the node value greater equal than x, node node to the greater.next
        """
        dummy = ListNode(None, head)

        start = dummy
        greater, greater_pointer = None, None
        current = head

        while current:
            val = current.val
            next_node = current.next

            if val >= x:
                if not greater_pointer:
                    greater = current
                    greater_pointer = greater
                else:
                    greater_pointer.next = current
                    greater_pointer = greater_pointer.next
            else:
                start.next = current
                start = start.next

            current = next_node

        if greater_pointer:
            greater_pointer.next = None

        start.next = greater

        return dummy.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Clearly solution, use two dummy node to store two linked nodes
        1. The value small than x nodes
        2. The value bigger than x nodes
        """
        dummy_head = ListNode(None, head)
        start = dummy_head

        dummy_greater = ListNode(None, None)
        greater = dummy_greater

        current = head
        while current:
            val = current.val
            next_node = current.next

            if val >= x:
                greater.next = current
                greater = greater.next
            else:
                start.next = current
                start = start.next

            current = next_node

        if greater:
            greater.next = None

        start.next = dummy_greater.next

        return dummy_head.next


if __name__ == "__main__":
    sol = Solution()

    # * Test case 1
    node = list_to_linked([1, 4, 3, 2, 5, 2])
    assert linked_to_list(sol.partition(head=node, x=3)) == [1, 2, 2, 4, 3, 5]

    # * Test case 2
    node = list_to_linked([2, 1])
    assert linked_to_list(sol.partition(head=node, x=2)) == [1, 2]

    # * Test case 3
    node = list_to_linked([1, 4, 3, 0, 5, 2])
    assert linked_to_list(sol.partition(head=node, x=2)) == [1, 0, 4, 3, 5, 2]

    # * Test case 4
    node = list_to_linked([])
    assert linked_to_list(sol.partition(head=node, x=0)) == []

    # * Test case 5
    node = list_to_linked([1])
    assert linked_to_list(sol.partition(head=node, x=2)) == [1]
