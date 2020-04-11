M = 10**6
s = [1 for i in range(M)]
for i in range(2,M/2):
    t = i+i
    while t<M:
        s[t]+=i
        t+=i

d = {}
for i in range(M):
    d[i] = []
    a = i
    while True:
        if s[a] not in d[i] and s[a]<M:
            d[i].append(s[a])
            a = s[a]
        else:
            break

f = [0 for i in range(M)]
m = [M for i in range(M)]
l = 2
ret = M
for i in range(2,M):
    if len(d[i])<=1:
        continue
    if s[d[i][-1]]==d[i][0]:
        f[i] = len(d[i])
        m[i] = min(d[i])
        if f[i]>l:
            l = f[i]
            ret = m[i]
        elif f[i]==l:
            ret = min(m[i],ret)
print f[220],f[12496]
print m[220],m[12496]
print l,ret
