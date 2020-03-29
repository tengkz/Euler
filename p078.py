d = {}
i=1
while True:
    s = 0
    d[(i,1)]=1
    d[(i,i)]=1
    for j in range(2,i):
        d[(i,j)] = 0
        for k in range(1,j+1):
            if k>i-j:
                break
            d[(i,j)]+=d[(i-j,k)]
        d[(i,j)]%=1000000
    for j in range(1,i+1):
        s+=d[(i,j)]
    if s%1000000==0:
        print i,s
        break
    print i,s
    i+=1

