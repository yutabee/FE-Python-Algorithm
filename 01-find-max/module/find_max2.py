from typing import List


def find_max(arr: List[int]) -> int:
    max_value = arr[0]
    n = len(arr)
    for i in range(1, n):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value


if __name__ == "__main__":
    input_arr = [3, 5, 2, 8, 1]
    print(find_max(input_arr))  # 8
