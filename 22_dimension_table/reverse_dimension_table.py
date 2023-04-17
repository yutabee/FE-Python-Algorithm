from typing import List


def create_dimension_table(rows: int, cols: int) -> None:
    # Create a new dimension table
    dimension: List[List[int]] = []
    for _ in range(rows):
        row: List[int] = []
        for _ in range(cols):
            row.append(0)
        dimension.append(row)

    # data set
    for i in range(rows):
        for j in range(cols):
            dimension[i][j] = (i + 1) * (j + 1)

    # print table
    for i in range(rows):
        for j in range(cols):
            print(f"{dimension[rows - 1 - i][cols -1 - j]:2}", end=" ")  # 反転
        print()


# 九九の表を作成して表示する（9x9）
create_dimension_table(9, 9)
