#coding:utf-8

def last9Digits(x):
    y = str(x%1000000000)
    return ''.join(sorted(list(y))) == '123456789'

def first9Digits(x):
    y = str(x)
    y = y[0:9]
    return ''.join(sorted(list(y))) == '123456789'

def fib(n):
    a=1
    b=0
    for i in range(n):
        yield a
        a,b = a+b,a

import time
start = time.time()
for i,f in enumerate(fib(500000)):
    if last9Digits(f) and first9Digits(f):
        print i+1
        break
end = time.time()
print end-start
