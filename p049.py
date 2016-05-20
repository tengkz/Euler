#coding:utf-8

import math
import itertools

def isSu(x):
    if x<=1:
        return False
    t = int(math.sqrt(x))
    for i in range(2,t+1):
        if x%i == 0:
            return False
    return True

s = "011233455677899"
r = list(itertools.combinations(s,4))
for item in r:
    x = list(itertools.permutations(item))
    tmp = []
    for y in x:
        t = int(''.join(y))
        if t>1000 and isSu(t):
            tmp.append(t)
    if len(tmp)<3:
        continue
    t1 = itertools.combinations(tmp,3)
    for k in t1:
        k1 = sorted(k)
        if k1[0] + k1[2] == (2*k1[1]):
            print k1
