import math

def isS(x):
    return int(math.sqrt(x))**2 == x

D = range(2,1001)
for d in D:
    if isS(d):
        D.remove(d)
x=2
while True:
    lenD = len(D)
    for d in D:
        t = x*x-1
        if t%d == 0 and isS(t/d):
            D.remove(d)
    x+=1
    tmp = len(D)
    if tmp!=lenD:
        print tmp,x
    if len(D) == 1:
        print D
        break
