"""
# 146
Medium
LRU Cache

https://leetcode.com/problems/lru-cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
* LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
* int get(int key) Return the value of the key if the key exists, otherwise return -1.
* void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
* 1 <= capacity <= 3000
* 0 <= key <= 10^4
* 0 <= value <= 10^5
* At most 2 * 10^5 calls will be made to get and put.

Reference:
https://www.romaglushko.com/blog/design-lru-cache/
"""

from typing import Optional


class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._remove_node(node)
        self._add_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.val = value
            self._remove_node(node)

        else:
            node = ListNode(key=key, val=value)

            if len(self.cache) >= self.capacity:
                self.cache.pop(self.tail.key)
                self._remove_node(self.tail)

        self.cache[key] = node
        self._add_to_head(node)

    def _add_to_head(self, node: ListNode) -> None:
        if self.head is not None:
            self.head.prev = node
            node.next = self.head

        if not self.tail:
            self.tail = node

        self.head = node

    def _remove_node(self, node: ListNode) -> None:
        if not node:
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        if self.head == node:
            self.head = next_node

        if self.tail == node:
            self.tail = prev_node

        node.prev = None
        node.next = None


if __name__ == "__main__":
    # * Test case 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    # * Test case 2
    lru = LRUCache(1)
    lru.put(2, 1)
    assert lru.get(2) == 1
