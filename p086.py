import math

s = 0

M = 1

while True:
    a = M
    a2 = a*a
    for b in range(1,a+1):
        b2 = b*b
        a2b2 = a2+b2
        for c in range(1,b+1):
            if math.sqrt(a2b2+c*c+2*b*c)%1==0:
                s+=1
    if s>1000000:
        print M
        break
    M+=1

print s
