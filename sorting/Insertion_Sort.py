def insertion_sort(num_list):
    length = len(num_list)
    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


if __name__ == '__main__':
    import random
    random_num_list = [random.choice(list(range(100))) for _ in range(10)]
    print(insertion_sort(random_num_list))