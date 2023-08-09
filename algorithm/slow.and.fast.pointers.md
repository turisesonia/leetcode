# Slow & Fast Pointers (Hare & Tortoise Algorithm)


### 作法
設定兩個指針以不同的速率遍歷 array, list or linked list
解決 "找尋中間值" (middle) 或者判斷 linked list 是否循環

### 範例
- Find middle node in Linked list
```
#  Linked list
1 -> 2 -> 3 -> 4 -> 5

使用兩種速率的指針 slow & fast, fast 的速度為 slow 的兩倍
所以當 fast 到達最後一個 node 時, slow 剛好會在 middle 的位置
```

```python
# head is linked list

slow = head
fast = head.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow
```



### Reference
- [快慢指針（Fast-slow Pointers）](https://hackmd.io/@Hsins/fast-slow-pointers#%E4%BE%8B%E9%A1%8C-%E9%8F%88%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%96%93%E7%B5%90%E9%BB%9E%EF%BC%88Middle-of-the-Linked-List%EF%BC%89)