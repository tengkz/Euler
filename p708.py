import math

M = 101
num = range(M)
factor_num = [0 for i in range(M)]

for i in range(2,M):
    if i%100000==0:
        print i
    if factor_num[i]==0:
        s = i
        while s<M:
            while num[s]%i==0:
                num[s]/=i
                factor_num[s]+=1
            s+=i

factor_num[0]=0
factor_num[1]=0

max_num = int(math.log(M)/math.log(2.0))

d = {}
for i in range(1,max_num+1):
    d[i] = factor_num.count(i)
other_prime = factor_num.count(0)-2
print factor_num[(M-100):M]
print num[(M-100):M]
print d
print other_prime

s = 1
for k,v in d.iteritems():
    s+=math.pow(2,k)*v
s+=2*other_prime

print s
