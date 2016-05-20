#coding:utf-8
import math

def isSu(a):
    if a<=1:
        return False
    for x in range(2,int(math.sqrt(a)+1)):
        if a%x==0:
            return False
    return True
def solve(a,b):
    cnt=0
    while isSu(cnt*cnt+a*cnt+b):
        cnt+=1
    return cnt

cnt = 0
ret = 0

for i in range(-999,999,2):
    print i
    if not isSu(abs(i)):
        continue
    for j in range(-999,999):
        tmp = solve(j,i)
        if tmp > cnt:
            cnt = tmp
            ret = i*j

print cnt,ret
