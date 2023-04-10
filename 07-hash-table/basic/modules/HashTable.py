class HashTable:
    """
    名前と電話番号を保存および検索するためのハッシュテーブルクラスです。
    """

    def __init__(self, size: int = 5):
        """
        HashTable クラスのインスタンスを初期化します。

        Args:
            size (int): ハッシュテーブルのサイズ。デフォルトは5。
        """
        self.size = size
        self.name = [None] * self.size
        self.tel = [None] * self.size

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

    def store(self, name: str, tel: str):
        """
        名前と電話番号をハッシュテーブルに格納します。

        Args:
            name (str): 格納する名前。
            tel (str): 格納する電話番号。
        """
        h = self._hash(name)
        self.name[h] = name
        self.tel[h] = tel
        print("ハッシュ値", h, "データ格納完了")

    def search(self, name: str) -> str:
        """
        指定された名前に関連付けられた電話番号を検索します。

        Args:
            name (str): 検索する名前。

        Returns:
            str: 電話番号（存在する場合）または None（存在しない場合）。
        """
        h = self._hash(name)
        if self.name[h] == name:
            return self.tel[h]
        else:
            return None
