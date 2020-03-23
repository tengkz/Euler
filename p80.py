import math

def fun(n):
    s = 0
    for i in range(1,101):
        a = 0.5*math.log10(n)+i
        b = math.pow(10.0,a)
        c = math.floor(b%10)
        print c
        s+=c
    return s

print fun(2)
