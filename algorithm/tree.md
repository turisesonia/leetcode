# Tree


### Tree Traversal
- 前序 (Preorder):
    root -> left -> right
    ```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

    1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
    ```

- 中序 (Inorder):
    left -> root -> right
    ```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

    4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
    ```

- 後序 (Postorder):
    left -> right -> root (From deep to top)
    ```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

    4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1
    ```