p = [0 for i in range(100000)]
p[0]=1
p[1]=1

def fun(n):
    res,k,a,b,s = 0,1,2,1,1
    while n>=a:
        res+=s*(p[n-a]+p[n-b])
        a+=3*k+2
        b+=3*k+1
        s*=-1
        k+=1
    res+=s*p[n-b] if n>=b else 0
    return res%1000000

n=2
while True:
    p[n] = fun(n)
    if p[n]==0:
        print n
        break
    n+=1
