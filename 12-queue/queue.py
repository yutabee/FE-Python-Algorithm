class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0

    def is_full(self):
        return (self.tail + 1) % self.max_size == self.head

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, data):
        if self.is_full():
            raise Exception("これ以上データを入れられません")
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail + 1) % self.max_size
            print(f"データ {data} を追加しました")

    def dequeue(self):
        if self.is_empty():
            raise Exception("取り出すデータが存在しません")
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            return data

    def display_status(self):
        print(f"キューの状態: {self.queue}")
        print(f"head: {self.head}, tail: {self.tail}\n")

if __name__ == "__main__":
    queue = Queue(6)

    for i in range(2,9):
        queue.display_status()
        try:
            queue.enqueue(i)
        except Exception as e:
            print(e)

    queue.display_status()

    for i in range(6):
        try:
            dequeued_data = queue.dequeue()
            queue.display_status()
            print(f"取り出したデータ {dequeued_data}")
        except Exception as e:
            print(e)
