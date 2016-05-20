#coding:utf-8

import math
import time

def isS(x):
    y = 24*x+1
    a = int(math.sqrt(y))
    if a*a != y:
        return False
    if (a+1)%6 == 0:
        return True
    return False

l = [1]
m = 10**9
s1 = time.time()
for i in range(2,10000):
    x = i*(3*i-1)/2
    for j in l[::-1]:
        if isS(x+j) and isS(x-j) and (x-j)<m:
            m = x-j
            break
    l.append(x)
s2 = time.time()
print m
print s2-s1
