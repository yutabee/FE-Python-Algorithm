from typing import List


def dijkstra_algorithm(graph: List[List[int]], start: int = 0):
    nodes_num: int = len(graph)  # ノードの数
    dist: List[int] = [F] * nodes_num  # 最短距離を格納する配列
    flags: List[int] = [0] * nodes_num  # 距離が確定したフラグに１を立てる
    current: int = start  # 現在処理しているノードのインデックス
    dist[current]: List[int] = 0  # スタート地点からcurrentまでの最短距離を格納する
    print("始点", current)

    for _ in range(nodes_num):
        d = F  # 隣接ノードへの最短距離を一時的に保持する変数(初期値99999)
        # 未確定の隣接ノードの中で最も距離が小さいノードを確定してcurrent_nodeとする
        for j in range(nodes_num):
            # フラグが未確 and ルートがある(F以下)
            if flags[j] == 0 and dist[j] < d:
                current = j  # 隣接ノードへの距離が最も小さい値でcurrentを更新
                d = dist[j]  # dを更新
        flags[current] = 1  # 最短距離のルートを確定 ->　確定したルートが次のcurrentノードへ

        for k in range(nodes_num):
            # current_nodeからk_node(現在位置からの隣接ノード)への距離が、隣接ノードへの現在の最短経路より短い場合
            if dist[current] + graph[current][k] < dist[k]:
                # k_nodeへの最短距離(ルートを更新)を更新
                dist[k] = dist[current] + graph[current][k]

    print("各ノードまでの距離")
    for i in range(nodes_num):
        print(f"ノード{i}まで {dist[i]}")


if __name__ == "__main__":
    F = 99999
    way = [
        [F, 3, 2, 5, F, F, F],
        [3, F, F, F, 7, F, F],
        [2, F, F, 2, F, 4, F],
        [5, F, 2, F, F, 1, F],
        [F, 7, F, F, F, 4, 5],
        [F, F, 4, 1, 4, F, 3],
        [F, F, F, F, 5, 3, F]
    ]

    dijkstra_algorithm(way, start=0)
