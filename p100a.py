import math
t = 1414213562373

i=0

while True:
    a = t+i
    if i%100000==0:
        print i
    x = 2*a*a-1
    y = math.sqrt(x)
    if x==int(y)*int(y):
        print a
        break
    i+=1
