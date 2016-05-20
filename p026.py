#coding:utf-8

def mod(a,b):
    while a<b:
        a*=10
    return a%b

def solve(x):
    length = 0
    tmp = [0]*x
    a = 1
    b = x
    t = mod(a,b)
    while t!=0:
        if tmp[t-1]==1:
            return sum(tmp)
        tmp[t-1]=1
        a=t
        t=mod(a,b)
ret = 0
flag = 0
for i in range(2,1000):
    tmp = solve(i)
    if tmp>ret:
        ret = tmp
        flag = i

print ret,flag
