M = 10**7
s = [1 for i in range(M)]

for n in range(2,M/2):
    if s[n]>1:
        continue
    t = n+n
    while t<M:
        r = 0
        temp = t
        while temp%n==0:
            r+=1
            temp/=n
        s[t]*=(r+1)
        t+=n

ret = 0
for i in range(2,M-1):
    if s[i]==s[i+1]:
        ret+=1
print ret
