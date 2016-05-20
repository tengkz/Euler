#coding:utf-8

def solve(x):
    y=str(x)
    if len(y)<9:
        return False
    t1 = list(y[0:9])
    t1.sort()
    t1 = ''.join(t1)
    if t1 != '123456789':
        return False
    t2 = list(y[-9:])
    t2.sort()
    t2 = ''.join(t2)
    if t2 != '123456789':
        return False
    return True

x=1
y=1
i=3

while not solve(x+y):
    t=x
    x=x+y
    y=t
    i+=1

print 'done'
print i

