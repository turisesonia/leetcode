from collections import deque


class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        """
        Args:
            value (int): TreeNode value.
            left (TreeNode, optional): Left node. Defaults to None.
            right (TreeNode, optional): Right node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, current: TreeNode):
        """
        比較 value 和 current.value 的大小,
        value 較小加到左節點
        value 較大加到右節點
        如果 ( 左 / 右 ) 節點均已存在, 則遞迴往下判斷

        Args:
            value (int): value
            current (TreeNode): Current node
        """

        node = TreeNode(value)

        if current.value > value:
            if not current.left:
                current.left = node
            else:
                self._insert(value, current.left)

        elif current.value < value:
            if not current.right:
                current.right = node
            else:
                self._insert(value, current.right)

        else:
            # value is exists
            print(f"value: {value} exists")

    def __repr__(self):
        return f"{self.root.value}"

    def in_order_traversal(self):
        """中序遍歷
        left -> root -> right
        """
        pass

    def pre_order_traversal(self):
        """前序遍歷
        root -> left -> right
        """
        pass

    def post_order_traversal(self):
        """後序遍歷
        left -> right -> root
        """
        pass

    def bfs_traversal(self):
        dq = deque([self.root])

        while len(dq) > 0:
            node = dq.popleft()

            if node.left:
                dq.append(node.left)

            if node.right:
                dq.append(node.right)

            print(node.value)
