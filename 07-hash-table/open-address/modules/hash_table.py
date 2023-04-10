"""
hash_table.py
"""


class HashTable:
    """
    名前と電話番号を保存および検索するためのハッシュテーブルクラスです。
    オープンアドレッシング法を用いて衝突を解決します。
    """
    def __init__(self, size):
        """
        HashTable クラスのインスタンスを初期化します。

        Args:
            size (int): ハッシュテーブルのサイズ。
        """
        self.size = size
        self.names = [None] * size
        self.phone_numbers = [None] * size

    def _hash(self, key: str) -> int:
        """
        文字列からハッシュ値を計算します（プライベートメソッド）。

        Args:
            key (str): ハッシュ値を計算するための文字列。

        Returns:
            int: 計算されたハッシュ値。
        """
        h = 0
        for i in key:
            h = h + ord(i)
        return h % self.size  # 計算されたハッシュをlistのindexの範囲にマッピング

    def insert(self, name, phone_number):
        """
        名前と電話番号をハッシュテーブルに格納します。

        Args:
            name (str): 格納する名前。
            phone_number (str): 格納する電話番号。
        """
        hash_index = self._hash(name)
        if self.names[hash_index] is None:
            self.names[hash_index] = name
            self.phone_numbers[hash_index] = phone_number
            print(f"Hash value: {hash_index}, data stored.")
        else:
            self.open_addressing(name, phone_number, hash_index)

    def open_addressing(self, name, phone_number, hash_index):
        """
        オープンアドレッシング法を使用して、名前と電話番号をハッシュテーブルに格納します。

        Args:
            name (str): 格納する名前。
            phone_number (str): 格納する電話番号。
            hash_index (int): ハッシュ値が衝突したインデックス。
        """
        is_open = False
        # ハッシュテーブルを走査
        for _ in range(self.size - 1):
            # hash_index + 1 -> if oversize -> mod
            hash_index = (hash_index + 1) % self.size
            if self.names[hash_index] is None:
                self.names[hash_index] = name
                self.phone_numbers[hash_index] = phone_number
                print(f"Rehashed: {hash_index}, data stored.")
                is_open = True
                return
        # ハッシュテーブルに空きがない場合
        if (not is_open):
            print("No available space to store data.")

    def search(self, name):
        """
        指定された名前に関連付けられた電話番号を検索します。

        Args:
            name (str): 検索する名前。

        Returns:
            str: 電話番号（存在する場合）または None（存在しない場合）。
        """
        hash_index = self._hash(name)
        if self.names[hash_index] == name:
            return self.phone_numbers[hash_index]
        elif self.names[hash_index] is None:
            return None
        else:
            return self.search_rehash(name, hash_index)

    def search_rehash(self, name, hash_index):
        """
        オープンアドレッシング法を使用して、指定された名前に関連付けられた電話番号を検索します。

        Args:
            name (str): 検索する名前。
            hash_index (int): ハッシュ値が衝突したインデックス。

        Returns:
            str: 電話番号（存在する場合）または None（存在しない場合）。
        """
        for _ in range(self.size - 1):
            hash_index = (hash_index + 1) % self.size
            if self.names[hash_index] == name:
                return self.phone_numbers[hash_index]
        return None
