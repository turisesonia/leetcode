"""
# 61
Medium
Rotate List

https://leetcode.com/problems/rotate-list

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg

Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:
* The number of nodes in the list is in the range [0, 500].
* -100 <= Node.val <= 100
* 0 <= k <= 2 * 10^9
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked, linked_to_list


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head

        # Find length of head linked
        length_of_link = 0
        current = head
        while current:
            current = current.next
            length_of_link += 1

        # 計算在第幾個 node 做搬動
        skip_count = length_of_link - (k % length_of_link)
        if skip_count == length_of_link:
            return head

        idx = 1
        dummy = ListNode(None, head)
        current = dummy.next

        while current:
            if idx == skip_count:
                new_head = current.next
                current.next = None
                dummy.next = new_head
                current = new_head
            elif idx == length_of_link:
                current.next = head
                current = None
            else:
                current = current.next

            idx += 1

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    node = sol.rotateRight(head=list_to_linked([1, 2, 3, 4, 5]), k=2)
    assert linked_to_list(node) == [4, 5, 1, 2, 3]

    node = sol.rotateRight(head=list_to_linked([0, 1, 2]), k=4)
    assert linked_to_list(node) == [2, 0, 1]

    node = sol.rotateRight(head=list_to_linked([1]), k=0)
    assert linked_to_list(node) == [1]

    node = sol.rotateRight(head=list_to_linked([1]), k=1)
    assert linked_to_list(node) == [1]

    node = sol.rotateRight(head=list_to_linked([1, 2]), k=2)
    assert linked_to_list(node) == [1, 2]
