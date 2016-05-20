#coding:utf-8

import math

def rvAdd(x):
    return x+int(str(x)[::-1])

def isPld(x):
    return x == int(str(x)[::-1])

cnt = 0
flag = 0
for i in range(1,10000):
    t = i
    flag = 0
    for j in range(50):
        t2 = rvAdd(t)
        if isPld(t2):
            flag = 1
            break
        else:
            t = t2
    if flag == 0:
        cnt+=1
print cnt
