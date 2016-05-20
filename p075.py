import math

s = [i**2 for i in range(0,1226)]
a = [0 for i in range(1500001)]
for i in range(1,1226):
    for j in range(i+1,1226):
        t = s[i] + s[j]
        if t in s:
            t1 = s.index(t)
            a[i+j+t1] += 1
cnt = 0
for i in range(1500001):
    if a[i] == 1:
        print i
print cnt
