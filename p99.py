import math

max_b = 0
max_e = 0
max_v = 0
max_i = 0

i = 1
for line in open('p099_base_exp.txt','r').readlines():
    b,e = line.strip().split(',')
    b,e = int(b),int(e)
    t = e*1.0*math.log(1.0*b)
    if t>max_v:
        max_v = t
        max_b = b
        max_e = e
        max_i = i
    i+=1

print max_b,max_e,max_i
