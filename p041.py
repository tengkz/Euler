#coding:utf-8

import math
import itertools
def isSu(x):
    for i in range(2,int(math.sqrt(x))):
        if x%i==0:
            return False
    return True
def solve(a):
    m=0
    for i in range(1,10):
        l = a[0:i]
        r = list(itertools.permutations(l))
        for item in r:
            t = int(''.join(item))
            if isSu(t) and t>m:
                m=t
    return m

a = '123456789'
print solve(a)

