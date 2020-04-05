M = 50
s = 0

for x1 in range(M+1):
    for y1 in range(M+1):
        if x1==0 and y1==0:
            continue
        for x2 in range(M+1):
            for y2 in range(M+1):
                if x2==0 and y2==0 or x1==x2 and y1==y2:
                    continue
                op = x1*x1+y1*y1
                oq = x2*x2+y2*y2
                pq = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
                if op+oq==pq or op+pq==oq or pq+oq==op:
                    s+=1

print s/2
