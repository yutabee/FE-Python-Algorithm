class LinkedList:
    def __init__(self, max_size=5):
        """
        LinkedList クラスの初期化メソッド

        Args:
            max_size (int, optional): リンクリストの最大サイズ. Defaults to 5.
        """
        self.data = [None] * max_size
        self.pointer = [None] * max_size
        self.head = 0
        self.max_size = max_size

    def add(self, item):
        """
        リンクリストに要素を追加するメソッド

        Args:
            item (any): 追加する要素

        Returns:
            bool: 追加に成功した場合は True, 失敗した場合は False
        """
        index = -1
        for i in range(self.max_size):
            if self.data[i] is None:
                index = i
                break

        if index == -1:
            print("データ領域に空きがありません")
            return False

        for i in range(self.max_size):
            if self.data[i] is not None and self.pointer[i] is None:
                self.pointer[i] = index
                break

        self.data[index] = item
        self.pointer[index] = None
        print("データ", item, "を追加しました")
        print("現在のリスト:", self.display())
        return True

    def delete(self, item):
        """
        リンクリストから要素を削除するメソッド

        Args:
            item (any): 削除する要素

        Returns:
            bool: 削除に成功した場合は True, 失敗した場合は False
        """
        index = -1
        for i in range(self.max_size):
            if self.data[i] == item:
                index = i
                break

        if index == -1:
            print("そのデータは存在しません")
            return False

        if index != self.head:
            for i in range(self.max_size):
                if self.pointer[i] == index:
                    self.pointer[i] = self.pointer[index]
        else:
            self.head = self.pointer[index]
            if self.head is None:
                self.head = 0

        self.data[index] = None
        self.pointer[index] = None
        print("データ", item, "を削除しました")
        print("現在のリスト:", self.display())
        return True

    def display(self):
        """
        リンクリストの要素を表示するメソッド
        """
        p = self.head
        while True:
            print(self.data[p], end="→")
            if self.pointer[p] is None:
                print("EOF")
                break
            p = self.pointer[p]
