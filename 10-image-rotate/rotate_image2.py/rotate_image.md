# 画像の回転について

画像の回転は、コンピュータグラフィックスや画像処理でよく使用される操作です。この記事では、画像の回転の基本概念や方法を説明し、実装例を提供します。

## 画像の回転の基本概念

画像の回転は、画像のピクセルを中心点を基準に特定の角度で回転させる操作です。以下は、画像の回転に関する一般的な操作です。

1. 左右反転
2. 上下反転
3. 左90度回転
4. 右90度回転

これらの操作は、2次元配列（画像のピクセル）に対して行われます。

## 実装方法

以下に、Pythonを使用した実装例を示します。この例では、画像を表す2次元配列に対して左右反転、上下反転、左90度回転、右90度回転の操作を行っています。

```python
from typing import List


def flip_horizontal(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    flipped_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            flipped_matrix[i][n - 1 - j] = matrix[i][j]
    return flipped_matrix


def flip_vertical(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    flipped_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_matrix[n - 1 - i][j] = matrix[i][j]
    return flipped_matrix


def flip_both(matrix: List[List[int]]) -> List[List[int]] :
    n = len(matrix)
    flipped_matrix = [[0]   * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]
    return flipped_matrix


def rotate_left(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[j][n - 1 - i]
    return rotated_matrix


def rotate_right(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[n - 1 - j][i]
    return rotated_matrix
```

これらの関数は、新しい2次元配列を作成し、元の画像のピクセルを適切な位置にコピーして操作を行っています。操作が完了したら、新しい配列を返しています。

## 使い方

以下は、これらの関数を使用して画像の回転操作を行う例です。

```python
image = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

flipped_horizontal_image = flip_horizontal(image)
flipped_vertical_image = flip_vertical(image)
rotated_left_image = rotate_left(image)
rotated_right_image = rotate_right(image)
```

これらの関数を使用して、`image`という2次元配列に対して左右反転、上下反転、左90度回転、右90度回転の操作を行っています。

## 注意事項

この実装例は、正方形の画像（行数と列数が同じ）に対してのみ機能します。矩形の画像（行数と列数が異なる）に対して操作を行う場合は、実装を適切に修正する必要があります。

また、この実装は画像のピクセル値が整数であると仮定していますが、実際の画像ファイル（PNG, JPEGなど）では、ピクセル値が異なるデータ型（例えば、3つのチャンネル（RGB）を持つタプルなど）を持つ場合があります。その場合は、適切なデータ構造と操作を実装に適用する必要があります。

## まとめ

画像の回転は、画像処理やコンピュータグラフィックスで一般的に使用される操作です。この記事では、画像の回転の基本概念と、Pythonを使用した実装例を提供しました。これらの知識と実装を参考に、画像の回転操作を独自のプロジェクトに適用できることを願っています。