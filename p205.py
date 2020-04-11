import itertools

num1 = 4**9
num2 = 6**6

s1 = [sum(t) for t in list(itertools.product([1,2,3,4],repeat=9))]
d1 = {}
for n in range(9,37):
    d1[n] = s1.count(n)

s2 = [sum(t) for t in list(itertools.product(range(1,7),repeat=6))]
d2 = {}
for n in range(6,37):
    d2[n] = s2.count(n)

ret = 0
for n1 in d1:
    for n2 in d2:
        if n1>n2:
            ret+=d1[n1]*d2[n2]

print sum(d1.values())
print sum(d2.values())
print num1,num2
print ret
print ret*1.0/(num1*num2)
