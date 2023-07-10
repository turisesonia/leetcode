from data_structure.binary_tree import BinarySearchTree


def test_binary_search_tree():
    tree = BinarySearchTree()

    for num in [10, 3, 15, 17, 7, 14, 5]:
        tree.insert(num)

    tree.bfs_traversal()