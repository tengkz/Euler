#coding:utf-8
import math

def ret(num,a,b,c):
    num2 = num%100
    max_1 = num2*100+99
    min_1 = num2*100
    max_a1 = int(math.ceil((math.sqrt(b*b-4*a*(c-max_1))-b)/(2*a)))
    min_a1 = int(math.floor((math.sqrt(b*b-4*a*(c-min_1))-b)/(2*a)))
    result = []
    for i in range(min_a1,max_a1+1):
        result.append(int(a*i*i+b*i+c))
    return result

for x in range(45,141):
    x1 = x*(x+1)/2
    r1 = ret(x1,1,0,0)
    for x2 in r1:
        if x2/100 != x1%100 or x2<1000:
            continue
        r2 = ret(x2,1.5,-0.5,0)
        for x3 in r2:
            if x3/100 != x2%100 or x3<1000:
                continue
            r3 = ret(x3,2,-1,0)
            for x4 in r3:
                if x4/100 != x3%100 or x4<1000:
                    continue
                r4 = ret(x4,2.5,-1.5,0)
                for x5 in r4:
                    if x5/100 != x4%100 or x5<1000:
                        continue
                    r5 = ret(x5,3,-2,0)
                    for x6 in r5:
                        if x6/100 != x5%100 or x6<1000:
                            continue
                        if x6%100 == x1/100:
                            print x1,x2,x3,x4,x5,x6
        
    
