import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from package import linked_list

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = linked_list.LinkedList()

    def test_insertFirst(self):
        self.linked_list.insertFirst(10)
        self.assertEqual(self.linked_list.toArray(), [10])

    def test_insertLast(self):
        self.linked_list.insertLast(20)
        self.assertEqual(self.linked_list.toArray(), [20])

    def test_insertAtIndex(self):
        self.linked_list.insertFirst(10)
        self.linked_list.insertAtIndex(1, 30)
        self.assertEqual(self.linked_list.toArray(), [10, 30])

    def test_indexOf(self):
        self.linked_list.insertFirst(10)
        self.assertEqual(self.linked_list.indexOf(10), 0)

    def test_contains(self):
        self.linked_list.insertFirst(10)
        self.assertTrue(self.linked_list.contains(10))

    def test_size(self):
        self.linked_list.insertFirst(10)
        self.assertEqual(self.linked_list.size(), 1)

    def test_removeFirst(self):
        self.linked_list.insertFirst(10)
        self.linked_list.removeFirst()
        self.assertEqual(self.linked_list.toArray(), [])

    def test_removeLast(self):
        self.linked_list.insertFirst(10)
        self.linked_list.removeLast()
        self.assertEqual(self.linked_list.toArray(), [])

    def test_removeAt(self):
        self.linked_list.insertFirst(10)
        self.linked_list.insertLast(20)
        self.linked_list.insertLast(30)
        self.linked_list.removeAt(1)
        self.assertEqual(self.linked_list.toArray(), [10, 30])

    def test_getPreviousNode(self):
        self.linked_list.insertFirst(10)
        self.linked_list.insertLast(20)
        self.assertEqual(self.linked_list.getPreviousNode(
            self.linked_list.last).value, 10)

    def test_print(self):
        self.linked_list.insertFirst(10)
        self.linked_list.insertLast(20)
        self.assertEqual(self.linked_list.print(), None)


if __name__ == '__main__':
    unittest.main()
