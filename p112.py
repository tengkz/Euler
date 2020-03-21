def fun(n):
    flag1 = 0
    flag2 = 0
    a = n%10
    n/=10
    while n>0:
        if n%10>a:
            flag1=1
        elif n%10<a:
            flag2=1
        a = n%10
        n=n/10
    if flag1==1 and flag2==1:
        return 1
    else:
        return 0

s = 0
num = 100
while s*1.0/num<0.99:
    num+=1
    s+=fun(num)
print num,s
