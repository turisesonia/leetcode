"""
# 2130
Medium
Maximum Twin Sum of a Linked List

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

Example 2:
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

Example 3:
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

Constraints:
The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 10^5
"""

from typing import Optional
from data_structure.linked import ListNode, list_to_linked


def pair_sum(head: Optional[ListNode]) -> int:
    """
    Intuitive solution.
    Retrieve the values from the lined list and store them in a 'nums' list.

    Sum twin indexes and find max value.
    """
    max_ = 0

    if not head:
        return 0

    nums = []

    current = head
    while current:
        nums.append(current.val)
        current = current.next

    nlen = len(nums)
    for i in range(nlen // 2):
        max_ = max(max_, nums[i] + nums[nlen - i - 1])

    return max_


def pair_sum(head: Optional[ListNode]) -> int:
    slow = head
    fast = head

    nums = []
    while fast:
        nums.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    max_, i = 0, len(nums) - 1
    while slow:
        max_ = max(max_, nums[i] + slow.val)

        slow = slow.next
        i -= 1

    return max_


def pair_sum(head: Optional[ListNode]) -> int:
    """
    nums: [1, 2, 3, 4, 5, 6] => twin: [(1, 6), (2, 5), (3, 4)]
    根據上面的 twin 規則可以看出，當抵達中間值後，將其中一半 subarray 倒序後，位置對應就是他的 twins

    利用快慢指針找到 Linked list 的中間位置，並且在找的同時建立一個 前半倒序的 linked list (prev)
    ```
    head = 1 -> 2 -> 3 -> 4 -> 5 -> 6
    slow = 1 -> 2 -> 3
    prev = 3 -> 2 -> 1
    ```

    完成後繼續移動 slow 指針並且與 prev 指針的值相加找到最大值
    """
    slow = head
    fast = head

    # reverse linked list
    # ex: head = 1 -> 2 -> 3 -> 4.  reverse = 4 -> 3 -> 2 -> 1
    prev = None

    while fast:
        # ! 要放第一個
        fast = fast.next.next

        temp = slow.next

        # 倒轉前半的 linked list
        slow.next = prev
        prev = slow

        slow = temp

    max_ = 0
    while slow:
        max_ = max(max_, slow.val + prev.val)

        slow = slow.next
        prev = prev.next

    return max_


if __name__ == "__main__":
    head = list_to_linked([5, 4, 2, 1, 8, 3])
    assert pair_sum(head) == 12

    head = list_to_linked([5, 4, 2, 1])
    assert pair_sum(head) == 6

    head = list_to_linked([4, 2, 2, 3])
    assert pair_sum(head) == 7

    head = list_to_linked([1, 100000])
    assert pair_sum(head) == 100001
