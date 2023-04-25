class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        # 追加した要素のインデックスを取得
        index = len(self.heap) - 1
        while index > 0:
            # 親要素のインデックス
            parent = (index - 1) // 2
            # 親要素の方が小さければbreak
            if self.heap[parent] <= self.heap[index]:
                break
            # 交換
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            # 操作対象のインデックスを上書き
            index = parent

    def find_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        # ヒープが空の場合
        if not self.heap:
            return None
        # ヒープの最小値を取り出す
        min_value = self.heap[0]
        # ヒープの最後の要素を最初に入れる
        self.heap[0] = self.heap[len(self.heap) - 1]
        # 最後の要素を取り除く
        self.heap.pop()

        # ヒープを再構築
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            # 子要素が存在する　and 子要素の方が小さければ -> インデックス交換
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            # 交換されなければbreak
            if smallest == index:
                break
            # 交換
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            # 操作対象のインデックスを上書き
            index = smallest

        # 最小の要素を返す
        return min_value


if __name__ == '__main__':
    # 使用例
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)

    print(min_heap.find_min())  # 5
    print(min_heap.extract_min())  # 5
