import math

def fun(n):
    f = int(math.floor(math.sqrt(n)))
    s = f
    i = len(str(s))
    f = f*10
    while i<100:
        n = n*100
        j = 0
        while j<=10:
            if (f+j)*(f+j)>n:
                break
            else:
                j+=1
        j-=1
        s+=j
        f = (f+j)*10
        i+=1
    return s

s = 0
for i in range(1,101):
    j = int(math.sqrt(i))
    if j*j==i:
        continue
    print i
    s+=fun(i)
print s
