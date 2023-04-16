def insertion_sort(numbers: list) -> list:
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


def sort_numbers_from_file(file_path: str) -> list:
    sorted_numbers = []
    file = open(file_path, 'r', encoding='utf-8')
    for line in file:
        number = int(line.strip())
        sorted_numbers.append(number)
        sorted_numbers = insertion_sort(sorted_numbers)
    file.close()
    return sorted_numbers


if __name__ == "__main__":
    file_path = "numbers.txt"  # ファイルパスを指定してください
    sorted_numbers = sort_numbers_from_file(file_path)
    print("Sorted numbers:", sorted_numbers)
