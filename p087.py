M = 7072
flag = [1 for i in range(M)]

for i in range(2,M):
    if flag[i]==1:
        s = i+i
        while s<M:
            flag[s]=0
            s+=i

primes = []
for n in range(2,M):
    if flag[n]==1:
        primes.append(n)

p1 = [i*i for i in primes if i<=7072]
p2 = [i*i*i for i in primes if i<=368]
p3 = [i*i*i*i for i in primes if i<=84]

lt = []
for t1 in p1:
    for t2 in p2:
        for t3 in p3:
            lt.append(t1+t2+t3)

print p3
st = set([item for item in lt if item<50000000])
print min(st)
print max(st)
print len(st)
