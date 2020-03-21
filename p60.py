import math
import itertools

def is_prime(n):
    n_s = int(math.sqrt(n*1.0))
    for i in range(2,n_s+1):
        if n%i==0:
            return 0
    return 1

num_list = range(10000000)
    
for i in range(2,10000000):
    if num_list[i]>0:
        t = 2*i
        while t<10000000:
            num_list[t]=0
            t+=i

prime_list = [i for i in num_list if i>0 and i!=1]
prime_set = set(prime_list)

def fun(s):
    l = len(s)
    for i in range(1,l):
        if s[i]=='0':
            continue
        a = int(s[:i])
        b = int(s[i:l])
        if a in prime_set and b in prime_set and int(str(b)+str(a)) in prime_set:
            return (a,b)
    return None

primes_list = []
for p in prime_list:
    ret = fun(str(p))
    if ret is not None:
        primes_list.append(ret)

primes_set = set(primes_list)

m = 999999999999
for p in itertools.combinations(primes_set,2):
    s1 = p[0]
    s2 = p[1]
    s3 = set([s1[0],s1[1],s2[0],s2[1]])
    if len(s3)!=4:
        continue
    if (s1[0],s2[0]) not in primes_set or (s1[0],s2[1]) not in primes_set or (s1[1],s2[0]) not in primes_set or (s1[1],s2[1]) not in primes_set:
        continue
    for prime in prime_set:
        if prime in s3:
            continue
        if (prime,s1[0]) in primes_set and (prime,s1[1]) in primes_set and (prime,s2[0]) in primes_set and (prime,s2[1]) in primes_set:
            print prime,s1[0],s1[1],s2[0],s2[1]
            s = prime+s1[0]+s1[1]+s2[0]+s2[1]
            if s<m:
                m = s
print m
