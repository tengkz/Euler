f = open('p059_cipher.txt','r')
s = f.read()
li = s.split(',')
li = [int(i) for i in li]

for x in range(97,123):
    for y in range(97,123):
        for z in range(97,123):
            t = [x,y,z]
            flag = 0
            for i in range(len(li)):
                a = li[i]^t[i%3]
                #if not (a>=65 and a<=90 or a>=97 and a<=122 or a in (32,39,44,46) or a>=48 and a<=57):
                if a>122:
                    flag+=1
                    break
            if flag==0:
                print [x,y,z]
