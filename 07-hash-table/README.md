# ハッシュテーブル

このプログラムは、Pythonでハッシュテーブルを実装したものです。ハッシュテーブルは、データを格納するためのデータ構造であり、キーと値のペアを保持します。このプログラムでは、名前と電話番号のペアをハッシュテーブルに格納し、名前を使って検索することができます。

## HashTableクラス

`HashTable` クラスは、ハッシュテーブルを表します。以下のメソッドを提供しています。

### `__init__(self, size)`

ハッシュテーブルのサイズを受け取り、指定されたサイズの空の配列を作成します。ここで、 `self.names` は名前を格納する配列であり、 `self.phone_numbers` は電話番号を格納する配列です。

### `calculate_hash(self, key)`

指定されたキーのハッシュ値を計算します。このプログラムでは、キーの各文字の Unicode 値の合計を取り、テーブルのサイズで割った余りをハッシュ値として使用しています。

### `insert(self, name, phone_number)`

名前と電話番号のペアをテーブルに挿入します。まず、 `calculate_hash` メソッドを使ってキーのハッシュ値を計算し、そのハッシュ値に対応するインデックスに名前と電話番号を格納します。もし既にそのインデックスにデータが格納されている場合は、`open_addressing` メソッドを呼び出して別の場所に格納します。

### `open_addressing(self, name, phone_number, hash_index)`

オープンアドレッシング法を使用して、既にインデックスにデータがある場合には、テーブル内の空きスペースを探してデータを格納します。

### `search(self, name)`

指定された名前の電話番号を検索します。まず、 `calculate_hash` メソッドを使ってキーのハッシュ値を計算し、そのハッシュ値に対応するインデックスに格納されている名前が指定された名前と一致する場合は、そのインデックスに格納されている電話番号を返します。名前が見つからない場合は、`None` を返します。インデックスにデータがあるが、指定された名前と一致しない場合は、 `search_rehash` メソッド呼び出して別の場所を検索します。

### `search_rehash(self, name, hash_index)`

オープンアドレッシング法を使用して、データがある場所から次々に次の場所を検索します。インデックスにデータがない場合は、最初に検索した場所に戻って `None` を返します。

## 実行例

以下は、このプログラムの実行例です。

```
hash_table = HashTable(5)

while True:
    name = input("Enter name: ")
    if name == "":
        break
    phone_number = input("Enter phone number: ")
    hash_table.insert(name, phone_number)

print(hash_table.names)
print(hash_table.phone_numbers)

while True:
    name = input("Enter name to search: ")
    if name == "":
        break
    phone_number = hash_table.search(name)
    if phone_number is None:
        print(f"{name} is not registered.")
    else:
        print(f"{name}'s phone number is {phone_number}.")
```

最初に、 `HashTable` オブジェクトを作成します。次に、 `insert` メソッドを使って名前と電話番号のペアをハッシュテーブルに挿入します。`insert` メソッドが成功すると、挿入されたデータのハッシュ値と格納されたインデックスが表示されます。

次に、 `search` メソッドを使って、指定された名前の電話番号を検索します。名前が見つかった場合は、その電話番号が表示されます。見つからなかった場合は、その旨が表示されます。

最後に、 `HashTable` オブジェクトに格納された名前と電話番号の配列が表示されます。