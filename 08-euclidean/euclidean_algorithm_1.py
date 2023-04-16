def euclidean_algorithm(a: int, b: int) -> int:
    """
    2つの整数 a, b の最大公約数を求める。

    Args:
        a: 整数
        b: 整数

    Returns:
        a, b の最大公約数
    """
    while b != 0:
        print(f"{a} ÷ {b} = {a // b} 余り {a % b}")
        a, b = b, a % b
    print(f"{a} ÷ {b} = {a}")
    return a


if __name__ == "__main__":
    print("a≧bとなる自然数を入力してください")
    a = int(input("a="))
    b = int(input("b="))
    gcd = euclidean_algorithm(a, b)
    print("それらの数の最大公約数は", gcd)
