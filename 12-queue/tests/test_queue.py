from queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_enqueue_dequeue(self):
        data = [1, 2, 3, 4]
        for d in data:
            self.queue.enqueue(d)

        for d in data:
            self.assertEqual(d, self.queue.dequeue())

    def test_empty_dequeue(self):
        with self.assertRaises(Exception) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), "取り出すデータが存在しません")

    def test_full_enqueue(self):
        data = [1, 2, 3, 4, 5]
        for d in data:
            self.queue.enqueue(d)

        with self.assertRaises(Exception) as context:
            self.queue.enqueue(6)
        self.assertEqual(str(context.exception), "これ以上データを入れられません")

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        data = [1, 2, 3, 4, 5]
        for d in data:
            self.queue.enqueue(d)
        self.assertTrue(self.queue.is_full())

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

if __name__ == "__main__":
    unittest.main()
