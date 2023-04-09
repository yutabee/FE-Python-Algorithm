"""
このモジュールは、整数のリストから最大値を見つける関数を提供します。

例:

    arr = [3, 5, 2, 8, 1]
    result = find_max(arr)
    print(result)  # 8 と出力される

このモジュールでは、型ヒントとドキュメントを追加しています。これにより、
関数の引数と戻り値の型が明確になり、関数の目的と使用方法がわかりやすくなります。
"""

from typing import List


def find_max(arr: List[int]) -> int:
    """
    配列内の最大値を返す関数です。

    Args:
        arr (List[int]): 整数のリスト。

    Returns:
        int: リスト内の最大値。
    """
    max_value = arr[0]  # 最初の要素を最大値と仮定
    for num in arr[1:]:  # 最初の要素をスキップしてループを開始
        if num > max_value:
            max_value = num  # より大きな値が見つかれば最大値を更新
    return max_value
