from typing import List, Optional


class Queue:
    def __init__(self, size: int = 5):
        self.size: int = size
        self.queue: List[Optional[int]] = [None] * size
        self.head: int = 0  # キューの先頭の位置 -> dequeueの操作位置
        self.tail: int = 0  # キューの末尾の位置 -> enqueueの操作位置

    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            print("データがいっぱいです")
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail + 1) % self.size
            print(f"データ {data} を追加しました")

    def dequeue(self):
        if self.head == self.tail:
            print("取り出すデータが存在しません")
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
            print(f"データ {data} を取り出しました")

    def display_status(self):
        print(f"キューの状態: {self.queue}")
        print(f"head: {self.head}, tail: {self.tail}\n")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue(11)
    q.dequeue()
