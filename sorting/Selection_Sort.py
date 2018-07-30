"""
Selection Sort
"""


def selection_sort(num_list):
    length = len(num_list)
    for i in range(0, length - 1):
        min_index = i
        for j in range(i + 1, length):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list


if __name__ == '__main__':
    import random

    random_num_list = random.choices(list(range(1000)), k=20)
    print(selection_sort(random_num_list))