#coding:utf-8

def reverseSum(x):
    return x+int(str(x)[::-1])
def allOdd(x):
    y=str(x)
    for c in y:
        if c not in ['1','3','5','7','9']:
            return False
    return True
cnt=0
for x in xrange(10**9):
    if x%10 != 0 and allOdd(reverseSum(x)):
        cnt+=1
print cnt
