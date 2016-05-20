#coding:utf-8

import itertools

s = "0123456789"

r = list(itertools.permutations(s))
ret = 0
for item in r:
    x = ''.join(item)
    t = int(x[1:4])
    if t%2 != 0:
        continue
    t = int(x[2:5])
    if t%3 != 0:
        continue
    t = int(x[3:6])
    if t%5 != 0:
        continue
    t = int(x[4:7])
    if t%7 != 0:
        continue
    t = int(x[5:8])
    if t%11 != 0:
        continue
    t = int(x[6:9])
    if t%13 != 0:
        continue
    t = int(x[7:10])
    if t%17 != 0:
        continue
    ret += int(x)
    print x

print ret
