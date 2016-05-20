#coding:utf-8

m = 123456789
for i in range(1,9876):
    s=str(i)
    for j in range(2,10):
        s+=str(i*j)
        if len(s)==9 and ''.join(sorted(s))=="123456789":
            t=int(s)
            if t>m:
                m=t
        elif len(s)>9:
            break
print m
