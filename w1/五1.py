def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 测试一个数是否为质数
num = int(input("请输入一个整数："))
if is_prime(num):
    print(f"{num} 是质数")
else:
    print(f"{num} 不是质数")






