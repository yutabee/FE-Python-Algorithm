import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack(max_size=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_overflow(self):
        stack = Stack(max_size=2)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())

    def test_underflow(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

if __name__ == '__main__':
    unittest.main()
