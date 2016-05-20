#coding:utf-8

import math
import itertools

def isCube(x):
    return int(x**(1.0/3))**3 == x
def cubeNum(x):
    s = str(x)
    p = list(itertools.permutations(s))
    cnt = 0
    for item in p:
        if isCube(int(''.join(item))):
            cnt+=1
    return cnt

i=406
while True:
    print i
    if cubeNum(i**3) == 5:
        print i
        break
    i+=1
