class Node(object):
    def __init__(self, value=None, left=None, right=None):
        """
        Args:
            value (optional): Node value. Defaults to None.
            left (Node, optional): Left node. Defaults to None.
            right (Node, optional): Right node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)

        else:
            self._insert(value, self.root)

    def _insert(self, value, current: Node):
        """比較 current.value 與傳進來的 value 大小,
        value 較小加到左節點
        value 較大加到右節點
        如果(左/右)節點已存在則遞迴往下判斷

        Args:
            value (): value
            current (Node): Current node
        """
        if current.value > value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)

        elif current.value < value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)
        else:
            # value is exists
            print(f"value: {value} exists")

    def __repr__(self):
        return f"{self.root.value}"

    def print_tree(self):
        self._print_node(self.root)

    def _print_node(self, current: Node):
        if current:
            print(current.value)
            self._print_node(current.left)
            self._print_node(current.right)

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


def demo():
    tree = BTree()

    for num in [10, 3, 15, 17, 7, 14, 5]:
        tree.insert(num)

    tree.print_tree()
