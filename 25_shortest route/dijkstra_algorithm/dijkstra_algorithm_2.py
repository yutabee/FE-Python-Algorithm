from typing import List


def dijkstra_algorithm(
        graph: List[List[int]],
        start: int = 0,
        goal: int = None):
    # 初期化
    nodes_num: int = len(graph)  # ノードの数
    dist: List[int] = [F] * nodes_num  # 最短距離を格納する配列
    routes: List[int] = [-1] * nodes_num  # 経路を格納する配列
    flags: List[int] = [0] * nodes_num  # 距離が確定したフラグに１を立てる
    current: int = start  # 現在処理しているノードのインデックス
    dist[current]: List[int] = 0  # スタート地点からcurrentまでの最短距離を格納する
    print("始点", current)

    for _ in range(nodes_num):
        d = F
        # 未確定の隣接ノードから、距離が最小となるノードを current_node に更新し、確定フラグを立てる
        for j in range(nodes_num):
            if flags[j] == 0 and dist[j] < d:
                current = j
                d = dist[j]
        flags[current] = 1

        # current_node is the goal
        if current == goal:
            break

        # 未確定の隣接ノードがcurrent_node を経由することで最短距離が小さくなる場合は最短距離を更新。
        for k in range(nodes_num):
            if flags[j] == 0:  # なくても更新はされないが計算量を減らせる
                if dist[current] + graph[current][k] < dist[k]:
                    dist[k] = dist[current] + graph[current][k]
                    routes[k] = current

    # 経路を
    path = []
    if goal is not None:
        current = goal
        while current != -1:  # 「-1」はスタートノード
            path.append(current)
            current = routes[current]
        path.reverse()

    return dist, path


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

    start_node = 0
    goal_node = 6
    distances, shortest_path = dijkstra_algorithm(way,
                                                  start=start_node,
                                                  goal=goal_node)
    print(f"ノード{goal_node}までの最短距離: {distances[goal_node]}")
    print(f"ノード{start_node}からノード{goal_node}までの最短経路: {shortest_path}")
