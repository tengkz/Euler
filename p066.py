#coding:utf-8
import math

def isS(x):
    return int(math.sqrt(x))**2 == x
def solve(D):
    y=1
    while True:
        if isS(y*y*D+1):
            return int(math.sqrt(y*y*D+1))
        y+=1

ret = []
for D in range(62,1001):
    if isS(D):
        continue
    tt = solve(D)
    ret.append(tt)
    print D,tt

print max(ret)
