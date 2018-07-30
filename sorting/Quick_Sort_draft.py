import random

# print(random.choices(list(range(100)),k=10))
num_list = [13, 91, 55, 39, 54, 44, 95, 37, 73, 77]


def quick_sort(num_list, left, right):
    if left < right:
        pivot_index = split_list(num_list, left, right)
        quick_sort(num_list, left, pivot_index - 1)
        quick_sort(num_list, pivot_index + 1, right)
    return num_list


def split_list(num_list, left, right):
    boundary = left
    # right = len(num_list)
    # pivot_value = num_list[len(num_list) // 2]
    # num_list[right], num_list[len(num_list) // 2] = num_list[len(num_list) // 2], num_list[right]
    pivot_value = num_list[(left+right) // 2]
    num_list[right], num_list[(left+right) // 2] = num_list[(left+right) // 2], num_list[right]
    # return num_list,pivot_value
    # print(num_list)
    for i in range(left, right):
        # print(num_list[i])
        if num_list[i] < pivot_value:
            num_list[boundary], num_list[i] = num_list[i], num_list[boundary]
            boundary += 1
    # print(boundary)
    # print(num_list)
    # print(pivot_value)
    # num_list[boundary], pivot_value = pivot_value, num_list[boundary]
    num_list[boundary], num_list[right] = num_list[right], num_list[boundary]
    # print(num_list)
    return boundary


print(split_list(num_list, 0, 9))
print(quick_sort(num_list, 0, len(num_list) - 1))
print(quick_sort(random.choices(list(range(100)),k=12),left=0,right=11))


def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p + 1, hi)
    return num_list


def partition(lst, lo, hi):
    pivot = lst[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi - 1] < lst[i + 1]:
        lst[i + 1], lst[hi - 1] = lst[hi - 1], lst[i + 1]
    return i + 1
# print(len(num_list))
# print(quicksort(num_list,0,len(num_list)))
