- [ヒープとは](#ヒープとは)
  - [ヒープの性質](#ヒープの性質)
  - [操作の効率](#操作の効率)
  - [ヒープの用途](#ヒープの用途)
  - [ヒープのインデックスの考え方](#ヒープのインデックスの考え方)
  - [主な操作](#主な操作)
- [ヒープの実装](#ヒープの実装)
  - [要素の追加](#要素の追加)
  - [要素の取り出し](#要素の取り出し)

# ヒープとは

### ヒープの性質

ヒープは、完全二分木であり、親ノードと子ノード間に特定の順序があるデータ構造です。

- **最小ヒープ**: 親ノードが子ノードよりも小さい（または等しい）
- **最大ヒープ**: 親ノードが子ノードよりも大きい（または等しい）

子ノード同士の大小関係は保証されていません。

### 操作の効率

- 最小値または最大値を効率的に取得・削除できるデータ構造。
- 挿入や削除操作は、O(log n) の時間複雑度で行うことができる。

### ヒープの用途

ヒープは、優先度付きキューとして使用されることが一般的です。
最小（または最大）値の効率的な取得・削除が必要なアルゴリズムやアプリケーションで活用されます。

### ヒープのインデックスの考え方

ヒープは、通常、**配列**を用いて実装されます。
親ノードのインデックスが i の場合、

- 左の子ノードのインデックスは `2i+1`、
- 右の子ノードのインデックスは `2i+2`
  （※ 最初のインデックスが 0 の場合）。

こんなイメージ！！！
`[i, 2i+ 1, 2i+2, 2(2i+1)+1, 2(2i+1)+2]`

逆に、子ノードのインデックスが j の場合、

- 親ノードのインデックスは`(j-1)// 2`。

### 主な操作

ヒープでは、主に以下の操作が行われます。

- **挿入**: 新しい要素を追加し、ヒープ条件を満たすように要素を並べ替える（アップヒープ操作）。
- **最小値（または最大値）の取得**: ルートノードの値を取得する。
- **最小値（または最大値）の削除**: ルートノードを削除し、最後の要素をルートノードに移動させ、ヒープ条件を満たすように要素を並べ替える（ダウンヒープ操作）。

これらのポイントを押さえておくことで、ヒープを理解しやすくなり、実装や適用がスムーズに行えるでしょう。

# ヒープの実装

Python では、ヒープはリストで実装されることが一般的です。以下に、最小ヒープの簡単な実装例を示します。

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        ...
```

## 要素の追加

1. 新しい要素をリストの末尾に追加します。
2. 親ノードの値が追加した要素以下になるまで、要素を入れ替えます。

※ ヒープは必ず左端のリーフから要素を追加する。(`self.heap.append(value)`)

```python
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
```

## 要素の取り出し

1. 最小ヒープから最小値（ルート要素）を取り出す。
2. 最後の要素をルートに持ってくる
3. ルートの要素を子要素と比較して適正な位置へ調整

```python
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
```
