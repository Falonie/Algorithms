import itertools


def bucket_sort(num_list):
    num = max(num_list) + 1
    bucket = [[_] for _ in range(num)]
    bucket_sequence = [[] for _ in range(num)]
    length = len(bucket)
    for i in num_list:
        for j in range(length):
            if i in bucket[j]:
                bucket_sequence[j].append(i)
    # print(bucket_sequence)
    # sorted_list = list(itertools.chain(*bucket_sequence))
    sorted_list = [m for _ in bucket_sequence for m in _]
    return sorted_list


if __name__ == '__main__':
    import random
    random_num_list = [random.choice(list(range(100))) for _ in range(10)]
    print(bucket_sort(random_num_list))
    test_case = [4, 64, 29, 99, 48, 73, 27, 57, 68, 33, 17, 41, 30, 92, 50, 1000, ]