#coding:utf-8
import itertools
dic = {}
dd = {}
i = 345
while True:
    s = ''.join(sorted(str(i**3)))
    if s in dic.keys():
        dic[s]+=1
        dd[s].append(i)
        if dic[s] == 5:
            print dd[s][0]
            break
    else:
        dic[s] = 1
        dd[s] = [i]
    i+=1
