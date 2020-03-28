def fun(n):
    s = str(n)
    if s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8' and s[16]=='9':
        return 1
    else:
        return 0

for i in range(101010101,138902662):
    s = i*i
    if fun(s)==1:
        print i
        break
