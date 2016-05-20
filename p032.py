#coding:utf-8
import itertools

def solve(s,ret):
        for i in range(1,6):
                for j in range(i+1,9):
                        a = int(''.join(s[0:i]))
                        b = int(''.join(s[i:j]))
                        c = int(''.join(s[j:]))
                        if a*b==c and c not in ret:
                                ret.append(c)
t = list(itertools.permutations('123456789'))
ret = []
cnt = 1
for item in t:
        print cnt
        cnt+=1
        solve(item,ret)
print sum(ret)

               
