def recursive_euclid(a: int, b: int) -> int:
    if b == 0:  # ベースケース
        return a
    else:  # 再帰処理
        return recursive_euclid(b, a % b)


if __name__ == "__main__":
    a = 88
    b = 66
    result = recursive_euclid(a, b)
    print(result)
