from operator import itemgetter

s = [1 for i in range(100001)]

for i in range(2,100001):
    if s[i]>1:
        continue
    s[i] = i
    t = i+i
    while True:
        if t<100001:
            s[t]*=i
            t+=i
        else:
            break

rad = [(s[i],i) for i in range(1,100001)]

rad = sorted(rad,key=itemgetter(0,1))

print rad[9999]
