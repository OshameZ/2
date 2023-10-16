import random


# 生成随机数列函数
def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return sorted(random_list)


# 选择排序函数
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 归并排序函数
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# 生成多组随机数列并排序
num_lists = 5  # 生成5组随机数列
list_lengths = [random.randint(10, 20) for _ in range(num_lists)]

for i, length in enumerate(list_lengths):
    random_list = generate_random_list(length)
    print(f"随机数列 {i + 1}: {random_list}")

    # 使用选择排序进行排序
    selection_sorted_list = random_list.copy()
    selection_sort(selection_sorted_list)
    print(f"选择排序后: {selection_sorted_list}")

    # 使用归并排序进行排序
    merge_sorted_list = random_list.copy()
    merge_sort(merge_sorted_list)
    print(f"归并排序后: {merge_sorted_list}")
    print()
