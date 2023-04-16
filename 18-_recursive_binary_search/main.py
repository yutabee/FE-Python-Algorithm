# pylint: disable=E0401, E0611
from modules.recursive_binary_search import recursive_binary_search


if __name__ == "__main__":
    data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    data.sort()
    a = recursive_binary_search(data, 65, 0, len(data)-1)
    print(a)
