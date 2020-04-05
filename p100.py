import math

x = 10**12

i = 0

while True:
    t = x+i
    t2 = t*t
    c = (t2-t)*2+1
    m = math.sqrt(c)
    n = int(m)
    if n*n==c:
        print t
        break
    i+=1
