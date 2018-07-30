num_list = [13, 91, 55, 39, 54, 44, 95, 37, 73, 77]


def quick_sort_in_place(num_list):
    if len(num_list) < 1:
        return num_list
    pivot = num_list[0]
    smaller_num = [_ for _ in num_list[1::] if _ < pivot]
    greater_num = [_ for _ in num_list[1::] if _ >= pivot]
    return quick_sort_in_place(smaller_num) + [pivot] + quick_sort_in_place(greater_num)


print(quick_sort_in_place(num_list))
