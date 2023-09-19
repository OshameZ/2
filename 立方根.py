import math
def func(n):
    result = math.pow(n,1/3)
    return int(result)
a=func(int(input("请输入一个整数:")))
print(a)
