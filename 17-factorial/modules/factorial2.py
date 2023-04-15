def factorial(n: int) -> int:
    value: int = 0

    print("入口", n)
    if n <= 1:  # ベースケース
        value = 1
    else:  # 再帰ステップ
        value = n * factorial(n - 1)
    print("出口", n, value)
    return value


if __name__ == "__main__":
    factorial(5)
