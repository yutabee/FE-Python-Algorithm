- [初心者のためのダイクストラアルゴリズム](https://qiita.com/knhr__/items/cb3ce311508337128714)

# dijkstra_algorithm01

このプログラムは、ダイクストラ法を実装してグラフ上のノード間の最短距離を求めるものです。関数`dijkstra_algorithm`は、グラフ（隣接行列形式）と始点ノードを引数に取ります。

---

### 手順

1. ノード数を取得し、最短距離を格納する配列`dist[int]`と、距離が確定したノードをフラグ付けする配列`flags[int]`を初期化。
2. 開始ノードを current_node に指定し、最短距離を 0 に設定。
3. current_node のすべての未確定の隣接ノードから、距離が最小となるノードを current_node に更新し、確定フラグを立てる。

```python
for j in range(nodes_num):
    # フラグが未確 and ルートがある(F以下)
    if flags[j] == 0 and dist[j] < d:
        current = j  # 隣接ノードへの距離が最も小さい値でcurrentを更新
        d = dist[j]  # dを更新
    flags[current] = 1  # 最短距離のルートを確定 ->　確定したルートが次のcurrentノードへ
```

4. current_node に隣接する未確定のノードについて調べ、<span style="color:red;font-weight:bold;">current_node を経由することで最短距離が小さくなる場合は最短距離を更新</span>。

```python
for k in range(nodes_num):
    # current_nodeの未確定の隣接ノードへの距離が、current_nodeを経由することで小さくなる場合
    if dist[current] + graph[current][k] < dist[k]:
        # k_nodeへの最短距離(ルートを更新)を更新
        dist[k] = dist[current] + graph[current][k]
```

5. ③、④ の手順を全てのノードが確定するまで繰り返す。

---
