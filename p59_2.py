f = open('p059_cipher.txt','r')
s = f.read()
li = s.split(',')
li = [int(i) for i in li]

t = [101,120,112]
s = 0
for i in range(len(li)):
    a = li[i]^t[i%3]
    s+=a
print s
