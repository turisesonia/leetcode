"""
# 2
Add Two Numbers
Medium

https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked


# v1
# def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]):
#     head = current = ListNode(None)
#     carry = False

#     while l1 or l2 or carry:
#         l1val = l1.val if l1 else 0
#         l2val = l2.val if l2 else 0

#         val = l1val + l2val

#         if carry:
#             val += 1

#         if val >= 10:
#             val = val % 10
#             carry = True
#         else:
#             carry = False

#         if l1:
#             l1 = l1.next

#         if l2:
#             l2 = l2.next

#         current.val = val

#         if l1 or l2 or carry:
#             current.next = ListNode(None)

#         current = current.next

#     return head


# v2
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    head = current = ListNode(None)
    carry = 0

    # 如果還有 linked 或 carry (進位) 不為 0 就繼續執行
    while l1 or l2 or carry > 0:
        # 取出值並相加
        l1val = l1.val if l1 else 0
        l2val = l2.val if l2 else 0

        val = l1val + l2val
        val += carry

        # 判斷是否有進位
        carry = val // 10
        # 如果 val >= 10 則進位留下個位數
        val = val % 10 if val >= 10 else val

        # l1, l2 個前進一個位置
        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

        current.val = val

        if l1 or l2 or carry:
            current.next = ListNode(None)

        current = current.next

    return head


if __name__ == "__main__":
    l1 = list_to_linked([2, 4, 3])
    l2 = list_to_linked([5, 6, 4])
    head = add_two_numbers(l1, l2)
    print(head)

    l1 = list_to_linked([0])
    l2 = list_to_linked([0])
    head = add_two_numbers(l1, l2)
    print(head)

    l1 = list_to_linked([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked([9, 9, 9, 9])

    head = add_two_numbers(l1, l2)
    print(head)
