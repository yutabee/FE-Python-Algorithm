## 木構造とは

木構造（tree structure）は、階層的なデータ構造の一つで、ノードと呼ばれる要素が親子関係を持ってつながっている構造です。一般的に、以下の特徴があります。

1. 一つの親ノードは複数の子ノードを持つことができます。
2. 各ノードは、一つの親ノードと、0 個以上の子ノードを持ちます。
3. 一番上のノードは根ノード（root node）と呼ばれ、親ノードを持ちません。
4. 子ノードを持たないノードは葉ノード（leaf node）と呼ばれます。

```
         A (根ノード)
       /   \
      B     C
     / \   / \
    D   E F   G (葉ノード)
```

## 木構造の種類

木構造にはいくつかの種類があります。主なものを以下に示します。

1. 二分木（binary tree）：各ノードが最大で 2 つの子ノードを持つ木構造
2. 二分探索木（binary search tree）：二分木のうち、各ノードに対して左の子孫ノードの値が現在のノードの値より小さく、右の子孫ノードの値が現在のノードの値より大きい条件を満たす木構造
3. AVL 木（AVL tree）：二分探索木のうち、どのノードに対しても左右の部分木の高さが最大でも 1 しか違わないように自動でバランスを取る木構造
4. ヒープ（heap）：完全二分木のうち、各ノードに対して親ノードの値が子ノードの値よりも大きい（最大ヒープ）または小さい（最小ヒープ）条件を満たす木構造

## Python での木構造の実装

Python で木構造を実装する際には、クラスを使ってノードを表現します。以下は、二分木を実装する例です。

```python
from typing import Optional, Any

class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# ノードを追加するメソッド
def insert(self, value: Any) -> None:
    if value < self.value:
        if self.left is None:
            self.left = TreeNode(value)
        else:
            self.left.insert(value)
    else:
        if self.right is None:
            self.right = TreeNode(value)
        else:
            self.right.insert(value)

# 木構造を表示するメソッド
def display(self, level: int = 0) -> None:
    if self.left:
        self.left.display(level + 1)
    print(' ' * 4 * level + str(self.value))
    if self.right:
        self.right.display(level + 1)
```

上記のコードでは、`TreeNode`クラスを定義し、二分木を実装しています。`insert`メソッドは、新しいノードを適切な位置に挿入するためのメソッドで、`display`メソッドは、木構造を表示するためのメソッドです。

以下は、上記の二分木クラスを使って木構造を作成し、表示する例です。

```python
# 木構造の作成
root = TreeNode(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)

# 木構造の表示
root.display()
```

出力結果：

```
        20
    30
        40
50
        60
    70
        80
```

このように、Python で木構造を実装する際には、クラスを使ってノードを表現し、各ノードに対して親子関係を定義することで、木構造を表現できます。今回紹介した二分木以外の木構造も、同様の方法で実装することができます。

# insert 解説

`insert`メソッドは、引数として渡された値を持つ新しいノードを、2 分探索木に適切な位置に挿入するためのメソッドです。以下に、メソッドの解説を行います。

```python
def insert(self, value: int) -> None:
    if value < self.value:
        if self.left is None:
            self.left = TreeNode(value)
        else:
            self.left.insert(value)  # recursive call
    else:
        if self.right is None:
            self.right = TreeNode(value)
        else:
            self.right.insert(value)  # recursive call
```

1. まず、引数として渡された`value`と、現在のノードの`self.value`を比較します。

   - `value`が`self.value`より小さい場合、左の子ノードに進む必要があります。
   - `value`が`self.value`より大きい場合、右の子ノードに進む必要があります。

2. 次に、進むべき方向（左または右）の子ノードが存在するかどうかを確認します。
   - 子ノードが存在しない場合（`None`の場合）、新しい`TreeNode`インスタンスを作成し、その子ノードとして設定します。
   - 子ノードが存在する場合、現在のノードから子ノードへと再帰的に`insert`メソッドを呼び出します。このプロセスは、適切な挿入位置が見つかるまで続きます。

# display 解説

`display`メソッドは、2 分探索木の構造をインデントを使って視覚的に表示するためのメソッドです。以下に、メソッドの解説を行います。

```python
def display(self, level: int = 0) -> None:
    if self.left:
        self.left.display(level + 1)
    print(' ' * 4 * level + str(self.value))
    if self.right:
        self.right.display(level + 1)
```

このメソッドでは、左から順にノードを表示しています。それぞれのノードの子ノードは、親ノードよりもインデントを 1 段階深く表示されます。

1. まず、左の子ノードが存在する場合、左の子ノードに対して`display`メソッドを再帰的に呼び出します。このとき、引数として渡された`level`に 1 を加算して、子ノードのインデントレベルを表します。

2. 次に、現在のノードの値を表示します。インデントの幅は、`level`に 4 を掛けた数のスペースで表現されます。これにより、木の階層が視覚的に表現されます。

3. 最後に、右の子ノードが存在する場合、右の子ノードに対して`display`メソッドを再帰的に呼び出します。同様に、引数として渡された`level`に 1 を加算して、子ノードのインデントレベルを表します。

この`display`メソッドを使用することで、2 分探索木の構造を簡単に視覚化することができます。ただし、木が大きくなると、表示が見づらくなることがあるため、デバッグや学習目的以外では、他の方法で木の構造を確認することをお勧めします。例えば、グラフ描画ライブラリを使用して、木を図示する方法が考えられます。
