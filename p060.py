import math
import itertools

def is_prime(n):
    n_s = int(math.sqrt(n*1.0))
    for i in range(2,n_s+1):
        if n%i==0:
            return 0
    return 1

num_list = range(100000000)
    
for i in range(2,100000000):
    if num_list[i]>0:
        t = 2*i
        while t<100000000:
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
            yield (a,b)
    yield None

primes_list = []
primes_dict = {}
for p in prime_list:
    for ret in fun(str(p)):
        if ret is not None:
            primes_list.append(ret)
            x,y = ret
            if x>y:
                x,y = y,x
            if x in primes_dict: 
                if y not in primes_dict[x]:
                    primes_dict[x].add(y)
            else:
                primes_dict[x] = set([y])

primes_set = set(primes_list)

m = 9999999
for p in primes_dict.keys():
    for p2 in primes_dict[p]:
        if p2 not in primes_dict:
            continue
        for p3 in primes_dict[p2]:
            if p3 not in primes_dict[p] or p3 not in primes_dict:
                continue
            for p4 in primes_dict[p3]:
                if p4 not in primes_dict[p] or p4 not in primes_dict[p2] or p4 not in primes_dict:
                    continue
                for p5 in primes_dict[p4]:
                    if p5 not in primes_dict[p] or p5 not in primes_dict[p2] or p5 not in primes_dict[p3]:
                        continue
                    s = p+p2+p3+p4+p5
                    if s<m:
                        print p,p2,p3,p4,p5
                        m = s
print m
            

#m = 999999999
#for p in itertools.combinations(primes_set,2):
#    s1 = p[0]
#    s2 = p[1]
#    s3 = set([s1[0],s1[1],s2[0],s2[1]])
#    if len(s3)!=4:
#        continue
#    if (s1[0],s2[0]) not in primes_set or (s1[0],s2[1]) not in primes_set or (s1[1],s2[0]) not in primes_set or (s1[1],s2[1]) not in primes_set:
#        continue
#    min_set = primes_dict[s1[0]].intersection(primes_dict[s1[1]]).intersection(primes_dict[s2[0]]).intersection(primes_dict[s2[1]])
#    if len(min_set)>0:
#        ss = s1[0]+s1[1]+s2[0]+s2[1]
#        for t in min_set:
#            ss2 = ss+t
#            if ss2<m:
#                print s1[0],s1[1],s2[0],s2[1],t
#                m = ss2
#
#print m
