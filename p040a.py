#coding:utf-8

s=''
for i in range(1,580000):
    s+=str(i)

for i in range(1,8):
    print s[(10**(i-1))-1]
