# KMP 演算法

## 問題
給定兩個字串 a, b
求 b 是否有出現在 a 之中 (即 b 是 a 的子字串) 並且找出在 a 的位置

Example: a = "abcabcdb", b = "abcd"
b 出現在 a[2] 和 a[5] 位置

## 解法

#### 暴力解
對每個位置做檢查，如果不對就將 a 就往下一個字元移動, b 回到開頭在重新逐個比較，
以此類推直到找到或沒找到為止

```
1.
✔✔✔✗
abcabcdb
abcd

2.
 ✗✗✗✗
abcabcdb
 abcd

3.
  ✗✗✗✗
abcabcdb
  abcd

4.
   ✔✔✔✔
abcabcdb
   abcd
```

#### 2. KMP
依照暴力解的範例，可以看到在第二次和第三次馬上就可以看到一定不相同 (因為第一個字元就不同了)
為了要不浪費時間去檢查這兩個一定錯的結果，

### 題目
 - [28. Find the Index of the First Occurrence in a String](../0028.find.the.index.of.the.first.occurrence.in.a.string.py)

### Reference

- [初學者學 KMP](https://yeefun.github.io/kmp-algorithm-for-beginners/)