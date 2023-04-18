import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append_and_display(self):
        linked_list = LinkedList()
        linked_list.append("apple")
        linked_list.append("banana")
        linked_list.append("cherry")
        self.assertEqual(linked_list.head.data, "apple")
        self.assertEqual(linked_list.head.next.data, "banana")
        self.assertEqual(linked_list.head.next.next.data, "cherry")

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append("apple")
        linked_list.append("banana")
        linked_list.append("cherry")

        linked_list.delete("banana")
        self.assertEqual(linked_list.head.data, "apple")
        self.assertEqual(linked_list.head.next.data, "cherry")

        linked_list.delete("apple")
        self.assertEqual(linked_list.head.data, "cherry")

        linked_list.delete("cherry")
        self.assertIsNone(linked_list.head)

    def test_empty_list(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        linked_list.delete("apple")
        self.assertIsNone(linked_list.head)


if __name__ == '__main__':
    unittest.main()
