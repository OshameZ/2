def fac(n):
    if n ==1:
        return 1
    else:
        return n*fac(n-1)
jc=fac(int(input("请输入一个整数：")))
print(jc)
