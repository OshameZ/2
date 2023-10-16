def construct_array_b(A):
    n = len(A)
    left = [1] * n
    right = [1] * n
    B = [1] * n

    # 计算左边的累积乘积
    for i in range(1, n):
        left[i] = left[i - 1] * A[i - 1]

    # 计算右边的累积乘积
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * A[i + 1]

    # 将左右两边的累积乘积相乘得到结果数组B
    for i in range(n):
        B[i] = left[i] * right[i]

    return B


# 示例用法
A = [1, 2, 3, 4]
B = construct_array_b(A)
print(B)  # 输出 [24, 12, 8, 6]
