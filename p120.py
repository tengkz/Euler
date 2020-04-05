def fun(a):
    a2 = a*a
    m = 0
    for n in range(1,a2+1):
        t = (2*n*a)%a2
        if t>m:
            m=t
    return m

result = 0
for i in range(3,1001):
    result+=fun(i)
print result
