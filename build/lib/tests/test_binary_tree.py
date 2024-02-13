from ..package import binary_tree
import unittest

import sys
import os

# Add the parent directory of 'project' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBinaryroot(unittest.TestCase):

    def setUp(self):
        self.root = binary_tree.Binaryroot()

    def test_insert_empty(self):
        self.root.insert(10)
        self.assertEqual(self.root.tree.data, 10)
        self.assertIsNone(self.root.tree.left)
        self.assertIsNone(self.root.tree.right)

    def test_insert_left(self):
        self.root.insert(10)
        self.root.insert(5)
        self.assertEqual(self.root.tree.data, 10)
        self.assertEqual(self.root.tree.left.data, 5)
        self.assertIsNone(self.root.tree.right)

    def test_insert_right(self):
        self.root.insert(10)
        self.root.insert(15)
        self.assertEqual(self.root.tree.data, 10)
        self.assertIsNone(self.root.tree.left)
        self.assertEqual(self.root.tree.right.data, 15)

    def test_insert_duplicate(self):
        self.root.insert(10)
        self.root.insert(10)
        self.assertEqual(self.root.tree.data, 10)
        # Expected behavior for duplicates depends on implementation;
        # here, we assume left bias
        self.assertEqual(self.root.tree.left.data, 10)
        self.assertIsNone(self.root.tree.right)

    def test_bfs_empty(self):
        self.assertEqual(self.root.bfs(None), [])

    def test_bfs_single_node(self):
        self.root.insert(10)
        self.assertEqual(self.root.bfs(self.root.tree), [10])

    def test_bfs_full_tree(self):
        self.root.insert(10)
        self.root.insert(5)
        self.root.insert(15)
        self.assertEqual(self.root.bfs(self.root.tree), [10, 5, 15])

    def test_dfs_empty(self):
        self.assertEqual(self.root.dfs(None), [])

    def test_dfs_single_node(self):
        self.root.insert(10)
        self.assertEqual(self.root.dfs(self.root.tree), [10])

    def test_dfs_full_tree(self):
        self.root.insert(10)
        self.root.insert(5)
        self.root.insert(15)
        self.assertEqual(self.root.dfs(self.root.tree), [10, 15, 5])

    def test_dfs_pre_order(self):
        self.root.insert(10)
        self.root.insert(5)
        self.root.insert(15)
        self.assertEqual(self.root.dfs_recursion(self.root.tree)[0], 10)
        self.assertEqual(self.root.dfs_recursion(self.root.tree)[1][0], 15)
        self.assertEqual(self.root.dfs_recursion(self.root.tree)[2][0], 5)


if __name__ == '__main__':
    unittest.main()
