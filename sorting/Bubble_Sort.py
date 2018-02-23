def bubble_sort(numlist):
    length = len(numlist)
    for i in range(length):
        for j in range(length - i - 1):
            if numlist[j] > numlist[j + 1]:
                numlist[j + 1], numlist[j] = numlist[j], numlist[j + 1]
    return numlist


if __name__ == '__main__':
    import random
    random_num_list = [random.choice(list(range(100))) for _ in range(10)]
    print(bubble_sort(random_num_list))