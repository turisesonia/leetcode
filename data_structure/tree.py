from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        """
        Args:
            val (int): TreeNode val.
            left (TreeNode, optional): Left node. Defaults to None.
            right (TreeNode, optional): Right node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node: {self.val}, Left: {self.left}, Right: {self.right}"

    def __str__(self):
        return str(self.val)


def list_to_binary_tree(items: list):
    n = len(items)

    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])

        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)

        return node

    return inner()


def binary_tree_to_list(root: TreeNode):
    from collections import deque

    res = []

    if not root:
        return res

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        res.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return res


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val: int, current: TreeNode):
        """
        比較 val 和 current.val 的大小,
        val 較小加到左節點
        val 較大加到右節點
        如果 ( 左 / 右 ) 節點均已存在, 則遞迴往下判斷

        Args:
            val (int): val
            current (TreeNode): Current node
        """

        node = TreeNode(val)

        if current.val > val:
            if not current.left:
                current.left = node
            else:
                self._insert(val, current.left)

        elif current.val < val:
            if not current.right:
                current.right = node
            else:
                self._insert(val, current.right)

        else:
            # val is exists
            print(f"val: {val} exists")

    def __repr__(self):
        return f"{self.root.val}"

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

            print(node.val)
