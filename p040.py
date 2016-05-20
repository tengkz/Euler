#coding:utf-8
def solve(x,a):
    cnt = 0
    while x>a[cnt] and x>a[cnt+1]:
        cnt+=1
    rem = x-a[cnt]
    t1 = rem/(cnt+2)
    t2 = rem%(cnt+2)
    if t2==0:
        t3 = a[cnt]+t1
    else:
        t3 = a[cnt]+t1+1
    print rem,t1,t2,t3
    return str(t3)[t2-1]

a = []
t = 0
for i in range(1,7):
    t+=9*(10**(i-1))*i
    a.append(t)

ret = 1
for i in range(1,7):
    ret*=int(solve(10**i,a))
print ret
