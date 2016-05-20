import math

def solve(a,b):
    while b!=1:
        if b==1:
            return False
        if a%b == 0:
            return False
        (a,b) = (b,a%b)
    return True

tmp = 0
flag = 0

for i in range(12,1000001):
    cnt = 0
    for j in range(2,i-1):
        if solve(i,j):
            cnt+=1
    t = i*1.0/cnt
    if t>tmp:
        tmp = t
print tmp
    
