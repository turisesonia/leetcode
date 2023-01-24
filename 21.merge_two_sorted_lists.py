"""
# 21
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def list_to_linked(ls: list):
    if len(ls) == 1:
        return ListNode(ls[0])

    return ListNode(ls[0], list_to_linked(ls[1:]))


def merge_two_sorted_list(list1: Optional[ListNode], list2: Optional[ListNode]):
    # 建立一個空的起始節點以及儲存現在位置路徑的變數
    head = current_path = ListNode(None)

    # 如果傳進來的兩個 linked list 都不為空
    # 開始判斷兩個節點的 val 大小
    while list1 and list2:
        if list1.val < list2.val:
            current_path.next = list1
            list1 = list1.next

        else:
            current_path.next = list2
            list2 = list2.next

        # 此次節點判斷結束，路徑往下一個移動
        current_path = current_path.next

    # 處理剩下的節點
    current_path.next = list1 or list2

    return head.next


if __name__ == "__main__":
    list1 = list_to_linked([1, 2, 4])
    list2 = list_to_linked([1, 3, 4])

    link = merge_two_sorted_list(list1, list2)

    while link is not None:
        print(link.val)
        link = link.next
