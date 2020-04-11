def fun(n):
    if n<=9:
        return n
    else:
        a = n/9
        b = n%9
        return ((b+1)*(10**a)-1)%1000000007

def big_number(n):
    a = n/9
    b = n%9
    print a,b
    s = (5*(10**a-1)-9*a)%1000000007
    s += ((b+2)*(b+1)/2*(10**a)-b-1)%1000000007
    return s%1000000007

f = [0 for i in range(91)]
f[1] = 1
for i in range(2,91):
    f[i]=f[i-1]+f[i-2]

print f

print big_number(1779979416004714189)
#ret = 0
#for i in f[2:]:
#    print i,f[i]
#    ret+=big_number(f[i])
#    ret%=1000000007
#
#print ret%1000000007
