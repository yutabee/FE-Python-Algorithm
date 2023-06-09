# 選択ソートの概要
1. リストの先頭要素を整列済みの部分、それ以外の要素を未整列の部分とします。
2. 未整列の部分が空になるまで以下の手順を繰り返します。
   1. 未整列の部分の先頭要素（以下、「キー」と呼びます）を取り出します。
   2. キーを整列済みの部分に挿入するために、整列済みの部分を右から左に向かって走査していきます。
      - 走査中の要素がキーより大きい場合、その要素を1つ右にずらします。これにより、キーを挿入するべき位置が1つ左になります。
      - 走査中の要素がキーより小さい場合、その要素の右隣がキーを挿入するべき位置です。走査を終了します。
   3. キーを適切な位置に挿入します。これにより、整列済みの部分が1つ要素が増え、未整列の部分が1つ要素が減ります。
3. 未整列の部分が空になったら、リスト全体が整列済みとなります。挿入ソートが完了です。

挿入ソートは、整列済みの部分を1つずつ拡大していくことでリスト全体を整列するアルゴリズムです。


# 解説
このコードは、挿入ソートアルゴリズムを用いて整数のリストを昇順にソートする機能を提供しています。挿入ソートは、リストの各要素を適切な位置に挿入することでソートを行うアルゴリズムです。

まず、挿入ソート関数`insertion_sort(arr: List[int]) -> List[int]:`は、整数のリスト`arr`を引数として受け取り、新しいソート済みリストを返します。この関数では元のリストを変更せず、新しいリスト`sorted_arr`にソートした結果を格納しています。`arr.copy()`を使用して`arr`のコピーを作成し、新しいリスト`sorted_arr`に割り当てています。

関数の中で、`n = len(sorted_arr)`によってリストの長さを取得します。その後、2つのネストされたforループを使用して挿入ソートを実行します。

- 外側のループ`for i in range(1, n):`は、ソート済み領域と未ソート領域の境界を移動します。
- 内側のループ`for j in range(i, 0, -1):`は、ソート済み領域の要素を1つずつ調べ、適切な位置に挿入するために未ソート領域から選択された要素（キー）を比較します。

内側のループ内で、キーがソート済み領域の要素より小さい場合（`if sorted_arr[j] < sorted_arr[j - 1]:`）、要素を交換します。これにより、キーはソート済み領域で適切な位置に挿入されます。要素の交換は、一時変数`tmp`を使用して行われます。

キーがソート済み領域の要素より大きい場合、内側のループを抜けます（`break`）。これは、すでにソート済み領域の要素が昇順になっているため、これ以上の交換が不要であることを意味します。

最後に、ソート済みのリスト`sorted_arr`が返されます。

このコードは、挿入ソートアルゴリズムの動作をトレースして表示するprint文も含んでいます。これにより、アルゴリズムの各ステップでの状態がわかりやすくなります。