# LinkedList

`LinkedList` は、固定サイズのリンクリストを実装する Python クラスです。データ要素とその要素間のリンク（ポインタ）を持ち、要素の追加や削除が容易に行えるデータ構造です。

## クラスメソッド

- `__init__(self, max_size=5)`:
  クラスの初期化メソッド。リンクリストの最大サイズを指定できます（デフォルトは 5）。

- `add(self, item)`:
  リンクリストに要素を追加するメソッド。追加に成功した場合は True を、失敗した場合は False を返します。

- `delete(self, item)`:
  リンクリストから要素を削除するメソッド。削除に成功した場合は True を、失敗した場合は False を返します。

- `display(self)`:
  リンクリストの要素を表示するメソッド。リストの先頭から順にデータ要素とリンク（ポインタ）を表示します。

## 使い方

```python
from linked_list import LinkedList

linked_list = LinkedList(5)  # 最大サイズ 5 のリンクリストを作成
for i in range(10, 70, 10):
    linked_list.add(i)  # 10 から 60 までの要素を追加

linked_list.delete(10)  # 要素 10 を削除
linked_list.display()   # リンクリストの要素を表示
```

# add関数解説
`add` 関数は、リンクリストに要素を追加するメソッドです。ここで、段階的に詳しく解説していきます。

1. 最初に、`index` という変数を -1 に初期化します。この変数は、データを格納する空きインデックスを格納するために使用されます。

```python
index = -1
```

2. 次に、`for` ループを使って、`data` リスト内の空きインデックスを探します。空きインデックスが見つかった場合、`index` にそのインデックスを代入し、ループを抜けます。

```python
for i in range(self.max_size):
    if self.data[i] is None:
        index = i
        break
```

3. 空きインデックスが見つからなかった場合（`index` が -1 のまま）、データ領域に空きがないというメッセージを表示し、False を返して処理を終了します。

```python
if index == -1:
    print("データ領域に空きがありません")
    return False
```

4. 空きインデックスが見つかった場合、次にポインタ（リンク）を更新する必要があります。`for` ループを使って、`pointer` リストを走査し、最後の要素（`pointer[i]` が None である要素）を見つけます。見つかった要素のポインタを、新しく見つけた空きインデックスに更新します。

```python
for i in range(self.max_size):
    if self.data[i] is not None and self.pointer[i] is None:
        self.pointer[i] = index
        break
```

5. 空きインデックスに新しい要素（`item`）を格納し、そのポインタを None に設定します。これで、新しい要素がリンクリストに追加されます。

```python
self.data[index] = item
self.pointer[index] = None
```

6. 最後に、新しい要素が追加されたことを示すメッセージを表示し、True を返して処理を終了します。

```python
print("データ", item, "を追加しました")
return True
```

この `add` 関数により、新しい要素をリンクリストに追加できます。また、リンクリストが最大サイズに達している場合は、追加できないことを示すメッセージが表示されます。

# delete関数
`delete` 関数は、リンクリストから要素を削除するメソッドです。ここで、段階的に詳しく解説していきます。

1. 最初に、`index` という変数を -1 に初期化します。この変数は、削除する要素のインデックスを格納するために使用されます。

```python
index = -1
```

2. 次に、`for` ループを使って、削除する要素（`item`）が `data` リスト内のどのインデックスにあるかを探します。要素が見つかった場合、`index` にそのインデックスを代入し、ループを抜けます。

```python
for i in range(self.max_size):
    if self.data[i] == item:
        index = i
        break
```

3. 要素が見つからなかった場合（`index` が -1 のまま）、そのデータが存在しないというメッセージを表示し、False を返して処理を終了します。

```python
if index == -1:
    print("そのデータは存在しません")
    return False
```

4. 要素が見つかった場合、次にポインタ（リンク）を更新する必要があります。削除する要素がリンクリストの先頭でない場合（`index` が `self.head` と異なる場合）、`for` ループを使って、`pointer` リストを走査し、削除する要素を指している要素（`pointer[i]` が `index` と等しい要素）を見つけます。見つかった要素のポインタを、削除する要素のポインタに更新します。

```python
if index != self.head:
    for i in range(self.max_size):
        if self.pointer[i] == index:
            self.pointer[i] = self.pointer[index]
```

5. 削除する要素がリンクリストの先頭である場合（`index` が `self.head` と等しい場合）、`self.head` を削除する要素のポインタに更新します。その後、`self.head` が None である場合、`self.head` を 0 に設定します。

```python
else:
    self.head = self.pointer[index]
    if self.head is None:
        self.head = 0
```

6. 要素を削除するため、`data` および `pointer` リストの対応するインデックスを None に設定します。

```python
self.data[index] = None
self.pointer[index] = None
```

7. 最後に、要素が削除されたことを示すメッセージを表示し、True を返して処理を終了します。

```python
print("データ", item, "を削除しました")
print("現在のリスト:", self.display())
return True
```

これにより、`delete` 関数は、リンクリストから指定された要素を削除し、リンクを適切に更新してリストを整えます。そして、リストの状態を表示して削除が成功したことをユーザーに伝えます。

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) のもとで公開されています。