def fun(n):
    s = str(n)
    s_reverse = s[::-1]
    if s==s_reverse:
        return 1
    else:
        return 0

li = [i*i for i in range(1,10001)]

result = 0
num = 0
m = {}
for i in range(2,10001):
    for j in range(10000-i):
        s = sum(li[j:(j+i)])
        if s>=100000000:
            break
        if fun(s)==1 and m.get(s,0)==0:
            result += s
            num += 1
            m[s] = 1
print result
print num
