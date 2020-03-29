# 10^8
d={1: 5761455, 2: 17427258, 3: 23727305, 4: 20959322, 5: 14371023, 6: 8493366, 7: 4600247, 8: 2367507, 9: 1180751, 10: 578154, 11: 279286, 12: 133862, 13: 63724, 14: 30143, 15: 14221, 16: 6644, 17: 3107, 18: 1430, 19: 661, 20: 297, 21: 133, 22: 62, 23: 25, 24: 11, 25: 4, 26: 1}


import math

M = 10001
num = range(M)
indice = [1 for i in range(M)]

for i in range(2,M):
    if indice[i]==1:
        s = i+i
        while s<M:
            indice[s]=0
            s+=i

indice[0]=0
indice[1]=0
num_prime = sum(indice)
prime = [0 for i in range(num_prime)]
t = 0
for i in range(M):
    if indice[i]==1:
        prime[t]=i
        t+=1
print num_prime
print prime
