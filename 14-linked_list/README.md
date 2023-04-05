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
from linkedlist import LinkedList

linked_list = LinkedList(5)  # 最大サイズ 5 のリンクリストを作成
for i in range(10, 70, 10):
    linked_list.add(i)  # 10 から 60 までの要素を追加

linked_list.delete(10)  # 要素 10 を削除
linked_list.display()   # リンクリストの要素を表示
```

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) のもとで公開されています。

このマークダウン形式の README ファイルでは、`LinkedList` クラスの概要、クラスメソッドの説明、使い方の例、およびライセンス情報を記載しています。これをプロジェクトのルートディレクトリに `README.md` という名前で保存することで、GitHub などのリポジトリで簡単にプロジェクトの説明を表示できます。