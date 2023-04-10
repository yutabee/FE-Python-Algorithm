class HashTable:
    """
    ハッシュテーブルを実装するクラスです。チェイン法を用いて衝突を解決します。
    """

    def __init__(self, size: int):
        """
        HashTableクラスのインスタンスを初期化します。

        Args:
            size (int): ハッシュテーブルのサイズ。
        """
        self.size = size
        self.hash_table = [None] * size // 2
        self.pointer = [None] * size // 2

    def _hash(self, key: int) -> int:
        """
        整数からハッシュ値を計算します（プライベートメソッド）。

        Args:
            key (int): ハッシュ値を計算するための整数。

        Returns:
            int: 計算されたハッシュ値。
        """
        h = 0
        h = key % self.size // 2
        return h

    def _rehash(self, h: int) -> int:
        """
        指定されたハッシュ値に対応するポインタを取得し、次のハッシュ値を計算します（プライベートメソッド）。

        Args:
            h (int): 現在のハッシュ値。

        Returns:
            int: 次のハッシュ値。
        """
        pointer = self.pointer[h]
        h = self.hash_table[pointer]
        return h

    def insert(self, data: int):
        """
        整数データをハッシュテーブルに挿入します。

        Args:
            data (int): 挿入する整数データ。
        """
        h = self._hash(data)

        if self.hash_table[h] is None:
            self.hash_table[h] = data
        else:
            while self.pointer[h] is not None:
                h = self.pointer[h]

            next_index = (h + 1) % (self.size // 2)
            while self.hash_table[next_index] is not None:
                next_index = (next_index + 1) % (self.size // 2)

            self.hash_table[next_index] = data
            self.pointer[h] = next_index

    def delete(self, data: int):
        """
        整数データをハッシュテーブルから削除します。データが見つからない場合、メッセージを表示します。

        Args:
            data (int): 削除する整数データ。
        """
        h = self.hash_search(data)

        if h == -1:
            print("Data not found.")
            return

        self.hash_table[h] = None

        prev_index = -1
        while h != -1:
            next_index = self.pointer[h]
            self.pointer[h] = prev_index
            prev_index = h
            h = next_index

    def hash_search(self, data: int) -> int:
        """
        指定された整数デ-タを検索し、見つかった場合はそのインデックスを返します。見つからない場合は-1を返します。

        Args:
            data (int): 検索する整数データ。

        Returns:
            int: データのインデックス（存在する場合）または -1（存在しない場合）。
        """
        h = self._hash(data)
        while self.hash_table[h] is not None:
            if self.hash_table[h] == data:
                return h
            else:
                h = self.pointer[h]

            if h is None:
                break

        return -1
