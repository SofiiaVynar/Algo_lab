import unittest

from main import BinaryTree, Diameter


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_empty_tree(self):
        root = BinaryTree()
        self.assertEqual(Diameter(root), 0)

    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertEqual(Diameter(root), 0)

    def test_example_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        self.assertEqual(Diameter(root), 6)


if __name__ == '__main__':
    unittest.main()
