"""binary search tree"""


def binary_search(array, start, end, item):
    mid = (start + end) // 2
    if array[mid] == item:
        return array[mid]
    elif array[mid] > item:
        print(array[mid])
        return binary_search(array, start, mid, item)
    elif array[mid] < item:
        print(array[mid])
        return binary_search(array, mid, end, item)


num_list = [13, 22, 24, 28, 31, 33, 34, 45, 58, 65, 71, 89]
print(binary_search(num_list, 0, len(num_list) - 1, 71))
