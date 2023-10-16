def Newton():
    c=10
    g=c/2
    i=0
    while(abs(g*g*g-c)>0.00000000001):
        g=2*g/3+c/(3*g*g)
        i+=1
        print("%d:%.13f"%(i,g))
Newton()