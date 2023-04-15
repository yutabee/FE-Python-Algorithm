# from modules.recursive_functions import factorial

# factorialの実行例
# print(factorial(5))  # 120

from modules.recursive_functions import binary_search

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 10, 22, 44, 55, 77]
    print(binary_search(arr, 0, len(arr) - 1, 5))  # 2