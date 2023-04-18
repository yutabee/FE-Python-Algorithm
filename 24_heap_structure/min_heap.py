class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1  # index of the last element
        while index > 0:
            parent = (index - 1) // 2  # *index of the parent*
            if self.heap[parent] <= self.heap[index]:
                break  # if the parent is smaller than the current element
            # exchange the value
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            # update the index to the parent
            index = parent

    def find_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        index = 0
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == index:
                break
            # exchange the value
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            index = smallest

        return min_value


if __name__ == '__main__':
    # 使用例
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)

    print(min_heap.find_min())  # 5
    print(min_heap.extract_min())  # 5
