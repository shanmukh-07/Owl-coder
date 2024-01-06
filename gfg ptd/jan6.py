# Techfest and the Queue
import math
def fun(n):
    ll = []
    s = 0
    while n%2 == 0:
        ll.append(2)
        s += 1
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            if fun(i):
                s += 1
            ll.append(i)
            n//=i
    if n>2:
        ll.append(n)
        s += 1
    return s
a,b = map(int,input().split())
ss = 0
for i in range(a,b+1):
    ss += fun(i)
print(ss)