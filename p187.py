M = 10**8
s = [1 for i in range(M)]

for n in range(2,M/2):
    if s[n]>1:
        continue
    print n
    t = n+n
    while t<M:
        r = 0
        temp = t
        while temp%n==0:
            r+=1
            temp/=n
        s[t]+=r
        t+=n

print s.count(3)
