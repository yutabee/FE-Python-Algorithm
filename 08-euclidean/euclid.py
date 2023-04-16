def euclid(a: int, b: int) -> int:
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return b


if __name__ == "__main__":
    a = 88
    b = 66
    result = euclid(a, b)
    print(result)
