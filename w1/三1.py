def conInt(n):
    s=[]
    while(n):
        s.append(str(n%2))
        n=n//2
    s.reverse()
    return "".join(s)

def conFra(n):
    x=[]
    s=[]
    while(n):
        n=n*2
        x.append(str(int(n)))
        n=n-int(n)
    for i in range(0,10):
        s.append(x[i])
    return "".join(s)


def main():
    n=eval(input())
    a=int(n)
    b=n-a
    print(f"{conInt(a)}.{conFra(b)}")

main()
