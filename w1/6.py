def Newton():
    c=int(input("请输入一个整数:"))
    g=c/4
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i+=1
        print("%d:%.13f"%(i,g))
Newton()