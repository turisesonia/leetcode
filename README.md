# Leedcode


## Unsolved
  - [0334 Increasing Triplet Subsequence](0334.increasing.triplet.subsequence.py)

  - [2352 Equal Row And Column Pairs](2352.equal.row.and.column.pairs.py)
    處理 `[[13, 13], [13, 13]]` case 時,
    hash map 會因為 key 相同而覆蓋 value

## Uncomprehended
  - [0007 Reverse Integer](0007.reverse.integer.py)

## Data structure & Algorithms

### Hash Map
  - [0001 Two Sum](0001.two.sum.py)
  - [0383 Ransom Node](0383.ransom.node.py)
  - [0387 First Unique Character In A String](0387.first.unique.character.in.a.string.py)
  - [0389 Find The Difference](0389.find.the.difference.py)
  - [0409 Longest Palindrome](0409.longest.palindrome.py)
  - [0500 Keyboard Row `Easy`](0500.keyboard.row.py)
  - [1464 Maximum Product Of Two Elements In An Array `Easy`](1464.maximum.product.of.two.elements.in.an.array.py)

### Array & Priority Queue (Heap)
  - [0056 Merge Intervals `Easy`](0056.merge.intervals.py)
  - [0215 Kth Largest Element In An Array `Medium` `Max Heap` `LeetCode 75`](0215.kth.largest.element.in.an.array.py)
  - [0506 Relative Ranks `Easy` `HashMap` `Max Heap`](0506.relative.ranks.py)
  - [0495 Teemo Attacking `Easy`](0495.teemo.attacking.py)

### Stack
  - [0003 Longest Substring Without Repeating Characters `Medium`](0003.longest.substring.without.repeating.characters.py)
  - [0394 Decode String `Medium`](0394.decode.string.py)
  - [0496 Next Greater Element I `Easy`](0496.next.greater.element.i.py)

### Linked List
  - [0002 Add Two Numbers](0002.add.two.numbers.py)
  - [0083 Remove Duplicates From Sorted List](0083.remove.duplicates.from.sorted.list.py)
  - [0141 Linked List Cycle](0141.linked.list.cycle.py)
  - [0169 Intersection Of Two Linked Lists](0160.intersection.of.two.linked.lists.py)
  - [0203 Remove Linked List Elements](0203.remove.linked.list.elements.py)
  - [0206 Reverse Linked List](0206.reverse.linked.list.py)
  - [0234 Palindrome Linked List](0234.palindrome.linked.list.py)
  - [2095 Delete The Middle Node Of A Linked List](2095.delete.the.middle.node.of.a.linked.list.py)
  - [2130 Maximum Twin Sum Of A Linked List `Medium` `LeetCode 75` `Slow Fast`](2130.maximum.twin.sum.of.a.linked.list.py)

### Binary Tree
  - [0094 Binary Tree Inorder Traversal `Easy`](0094.binary.tree.inorder.traversal.py)
  - [0100 Same Tree](0100.same.tree.py)
  - [0101 Symmetric Tree](0101.symmetric.tree.py)
  - [0102 Binary Tree Level Order Traversal `Medium` `BFS`](0102.binary.tree.level.order.traversal.py)
  - [0103 Binary Tree Zigzag Level Order Traversal `Medium` `BFS`](0103.binary.tree.zigzag.level.order.traversal.py)
  - [0104 Maximum Depth Of Binary Tree](0104.maximum.depth.of.binary.tree.py)
    > Stack 解法比較容易理解 (DFS)
  - [0107 Binary Tree Level Order Traversal II `Medium` `BFS`](0107.binary.tree.level.order.traversal.ii.py)
  - [0108 Convert Sorted Array To Binary Search Tree](0108.convert.sorted.array.to.binary.search.tree.py)
  - [0110 Balanced Binary Tree](0110.balanced.binary.tree.py)
  - [0111 Minimum Depth Of Binary Tree](0111.minimum.depth.of.binary.tree.py)
    > Queue 解法較容易理解, 只要找到第一個 leaf node 即為最小深度
  - [0112 Path Sum `Easy` `DFS`](0112.path.sum.py)
    > Stack 解法較容易理解
  - [0113 Path Sum II `Medium` `DFS`](0113.path.sum.ii.py)
  - [0144 Binary Tree Preorder Traversal](0144.binary.tree.preorder.traversal.py)
  - [0145 Binary Tree Postorder Traversal](0145.binary.tree.postorder.traversal.py)
  - [0199 Binary Tree Right Side View `Medium` `BFS` `LeetCode 75`](0199.binary.tree.right.side.view.py)
  - [0222 Count Complete Tree Nodes](0222.count.complete.tree.nodes.py)
  - [0226 Invert Binary Tree](0226.invert.binary.tree.py)
  - [0257 Binary Tree Path](0257.binary.tree.path.py)
  - [0404 Sum Of Left Leaves `Easy` `DFS`](0404.sum.of.left.leaves.py)
  - [0437 Path Sum III `Medium` `DFS`](0437.path.sum.iii.py)
    > 看起來必須要使用遞迴才能解，需複習
  - [0450 Delete Node In A Bst `Medium` `DFS` `BST`](0450.delete.node.in.a.bst.py)
    > 要了解 Inorder successor node，需複習
  - [0700 Search In A Binary Search Tree `Easy` `BST` `LeetCode 75`](0700.search.in.a.binary.search.tree.py)
  - [0872 Leaf Similar Trees](0872.leaf.similar.trees.py)
  - [1161 Maximum Level Sum Of A Binary Tree `Medium` `BFS` `LeetCode 75`](1161.maximum.level.sum.of.a.binary.tree.py)
  - [1372 Longest Zigzag Path In A Binary Tree `Medium` `DFS`](1372.longest.zigzag.path.in.a.binary.tree.py)
    > 遞迴、並在連續方向時將先前的路徑總和重設為 0
  - [1448 Count Good Nodes In Binary Tree `Medium` `LeetCode 75`](1448.count.good.nodes.in.binary.tree.py)


### Graph
  - [0547 Number Of Provinces `Medium` `DFS` `LeetCode 75` `Need Review`](0547.number.of.provinces.py)
    > 先找出相連的物件並將已訪問過的物件記錄起來，最後再將沒走訪過的元素再檢查一次
  - [0841 Keys And Rooms `Medium` `DFS` `LeetCode 75`](0841.keys.and.rooms.py)

### Two Pointers
  - [0005 Longest Palindrome `Medium`](0005.longest.palindrome.py)

### Binary Search
  - [0162 Find Peak Element `Medium` `LeetCode 75`](0162.find.peak.element.py)
  - [0374 Guess Number Higher Or Lower `Easy` `LeetCode 75`](0374.guess.number.higher.or.lower.py)
  - [0441 Arranging Coins `Easy`](0441.arranging.coins.py)
  - [0875 Koko Eating Bananas `Medium` `LeetCode 75`](0875.koko.eating.bananas.py)
  - [2300 Successful Pairs Of Spells And Potions `Medium` `LeetCode 75`](2300.successful.pairs.of.spells.and.potions.py)

### Sliding Window
  - [1493 Logest Subarray Of 1's After Deleting One Element `Medium`](1493.logest.subarray.of.1's.after.deleting.one.element.py)


### Dynamic Programming 動態規劃
  - [0014 Longest Common Prefix](0014.longest.common.prefix.py)
  - [0053 Maxunum Subarry](0053.maxunum.subarry.py)
  - [0070 Climbing Stairs](0070.climbing.stairs.py)
  - [0303 Range Sum Query Immutable `Easy`](0303.range.sum.query.immutable.py)

### Greedy Algorithm 貪婪演算法
  找出當下所有選擇中的最佳解
  - [0455 Assign Cookies](0455.assign.cookies.py)