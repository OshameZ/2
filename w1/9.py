import random
import math
def f(x):
    return x**2+4*x*math.sin(x)
a=2
b=3
N=1000000
count = 0
for i in range(N):
    x=random.uniform(a,b)
    y=random.uniform(0,f(b))
    if y<= f(x):
        count+=1
integral=(b-a)*21*count/N
print("积分结果：",integral)

