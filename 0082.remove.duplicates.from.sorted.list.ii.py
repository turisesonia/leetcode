"""
# 82
Medium
Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:

https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
* The number of nodes in the list is in the range [0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional
from data_structure.linked import ListNode, linked_to_list, list_to_linked


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # 宣告一個假的 Node 當成開頭，用來處理 head 開始就有重複的狀況
        dummy = ListNode(None, head)

        # 不重複 node 的前一個位置
        start = dummy

        # prev / current 用來判斷是否出現重複的 node
        prev = head
        current = head.next
        duplicate = False

        while current:
            if prev.val == current.val:
                duplicate = True

            else:
                prev = current

                # 如果有之前有判斷到出現重複的 node, 則將 start.next 指到現在不重複的 node 上
                if duplicate:
                    start.next = current
                else:
                    start = start.next

                duplicate = False

            current = current.next

        if duplicate:
            start.next = current

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    head = list_to_linked([1, 2, 3, 3, 4, 4, 5])
    node = sol.deleteDuplicates(head)
    assert linked_to_list(node) == [1, 2, 5]

    head = list_to_linked([1, 1, 1, 2, 3])
    node = sol.deleteDuplicates(head)
    assert linked_to_list(node) == [2, 3]

    head = list_to_linked([1, 1])
    node = sol.deleteDuplicates(head)
    assert linked_to_list(node) == []
