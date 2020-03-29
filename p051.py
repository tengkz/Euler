import math

def is_prime(n):
    sn = int(math.sqrt(n))
    for i in range(2,sn+1):
        if n%i==0:
            return 0
    return 1

def fun_0(s):
    number = 0
    for d in '123456789':
        t = int(s.replace('0',d))
        if is_prime(t)==1:
            number += 1
    return number

def fun_1(s):
    number = 0
    for d in '23456789':
        t = int(s.replace('1',d))
        if is_prime(t)==1:
            number+=1
    return number

def fun_2(s):
    number = 0
    for d in '3456789':
        t = int(s.replace('2',d))
        if is_prime(t)==1:
            number+=1
    return number

i = 56004
while True:
    if is_prime(i)==0:
        i+=1
        continue
    s = str(i)
    if '0' in s and fun_0(s)==7:
        print s
        break
    if '1' in s and fun_1(s)==7:
        print s
        break
    if '2' in s and fun_2(s)==7:
        print s
        break
    i+=1
