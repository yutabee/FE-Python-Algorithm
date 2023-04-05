class Stack:
    def __init__(self, max_size=5):
        self._max_size = max_size
        self._stack = [0] * max_size
        self._sp = 0

    def push(self, data):
        if self._sp < self._max_size:
            self._stack[self._sp] = data
            self._sp += 1
            print("データ", data, "を追加しました")
            self.print_stack()
        else:
            print("これ以上データを入れられません")

    def pop(self):
        if self._sp > 0:
            self._sp -= 1
            data = self._stack[self._sp]
            print("取り出したデータ", data)
            self.print_stack()
            return data
        else:
            print("取り出すデータが存在しません")
            return None

    def print_stack(self):
        print("スタックの状態:", self._stack[:self._sp])