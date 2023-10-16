def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 从第二个元素开始，将当前元素插入已排序的部分
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            # 向右移动已排序的元素，直到找到合适的位置
            arr[j + 1] = arr[j]
            j -= 1

        # 将当前元素插入到合适的位置
        arr[j + 1] = key


# 测试排序算法
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("排序后的数组:", arr)
