"""
# 160
Easy
Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
If you correctly return the intersected node, then your solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""

from typing import Optional
from data_structure.linked_list import ListNode, list_to_linked


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    先找到 headA 和 headB 的最後一個 node, 同時計算長度
    如果這兩個 node 不相同, 代表這兩個 linked list 沒有交集

    確定 headA, headB 有交集後, 開始從頭檢查
    因為在交集時的 linked list 長度會是一樣的
    所以我們檢查 node 是不是交集時從, 長度一樣的時候再檢查就好

    Ex:
    headA : 4 -> 1 -> 8 -> 4 -> 5
    headB : 5 -> 6 -> 1 -> 8 -> 4 -> 5

    headA length = 5
    headB length = 6

    交集處在 8

    因 headB 比 headA 長一個 node
    所以 headB 跳過第一個 node 後, 才開始每個 node 和 headA 做相等檢查
    直到找到 8 即為答案
    """
    last_a, last_b = headA, headB
    len_a, len_b = 1, 1

    while last_a.next:
        last_a = last_a.next
        len_a += 1

    while last_b.next:
        last_b = last_b.next
        len_b += 1

    if last_a != last_b:
        return None

    cur_a, cur_b = headA, headB

    while cur_a and cur_b:
        if len_a > len_b:
            cur_a = cur_a.next
            len_a -= 1
            continue

        if len_b > len_a:
            cur_b = cur_b.next
            len_b -= 1
            continue

        if cur_a == cur_b:
            return cur_a
        else:
            cur_a = cur_a.next
            cur_b = cur_b.next


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Hashmap 解法

    存下 headA 所有的 node 到 appeared 內
    再檢查 headB 是否有一樣的 node
    """
    appeared = set()

    while headA:
        appeared.add(headA)
        headA = headA.next

    while headB:
        if headB in appeared:
            return headB
        headB = headB.next

    return None


if __name__ == "__main__":
    intersect = list_to_linked([8, 4, 5])
    a = list_to_linked([4, 1])
    a.next.next = intersect

    b = list_to_linked([5, 6, 1])
    b.next.next.next = intersect

    assert get_intersection_node(a, b) == intersect

    a = list_to_linked([2, 6, 4])
    b = list_to_linked([1, 5])

    assert not get_intersection_node(a, b)
