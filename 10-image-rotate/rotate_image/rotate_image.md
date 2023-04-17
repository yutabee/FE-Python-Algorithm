
# 回転アルゴリズムの概要

2次元配列を回転させるアルゴリズムは、以下の手順で実行できます。

1. 配列を転置する（行と列を入れ替える）。
2. 各行を反転する（左右反転させる）。

この手順により、90度回転した図形を得ることができます。

## 実装例

以下は、2次元配列を回転させるアルゴリズムの実装例です。

```python
def rotate(matrix):
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix
```

## 使用方法

以下は、このアルゴリズムを使用して2次元配列を回転させる例です。

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate(matrix)
print(rotated_matrix)
```

実行結果：

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

この例では、与えられた2次元配列（`matrix`）が90度回転して新しい配列（`rotated_matrix`）になっています。

## 注意点

- 上記のアルゴリズムは、正方形の2次元配列（行数と列数が同じ）にのみ適用可能です。長方形の配列に適用する場合は、アルゴリズムの調整が必要です。
- このアルゴリズムは90度回転のみに対応しています。180度や270度など、他の角度で回転させる場合は、アルゴリズムを複数回適用するか、別の方法を検討してください。