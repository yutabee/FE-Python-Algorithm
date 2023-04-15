"""
fucotrial.py
"""


def factorial(n):  # pylint: disable=invalid-name
    """
    引数 n の階乗を計算します。

    パラメータ
    ----------
    n : int
        階乗を計算する整数 (0 以上)

    戻り値
    -------
    int
        n の階乗 (n!)

    例外
    -----
    ValueError
        n が負の整数の場合

    例
    ----
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n < 0:
        raise ValueError("n は0以上の整数でなければなりません")
    if n == 0 or n == 1:  # ベースケース
        return 1
    else:  # 再帰ステップ
        return n * factorial(n - 1)
