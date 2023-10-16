n=int(input("请输入正整数："))
if n==1 or n==2:
    print(n)
if n %3 == 0:
    a = int(n/3)
    print("{}个3".format(a))
if n % 3 == 1:
    b =int( n/3 -1)
    print("{}个3和1个4".format(b))
if n % 3 == 2:
    c =int( n / 3)
    print("{}个3".format(c))
