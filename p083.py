content = open('p083_matrix.txt','r').readlines()

data = []
for line in content:
    line = [int(num) for num in line.strip().split(',')]
    data.append(line)

#data = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

M = len(data)

ret = [[0 for i in range(M)] for j in range(M)]

# initialize
ret[0][0] = data[0][0]
for i in range(1,M):
    ret[i][0] = ret[i-1][0]+data[i][0]
    ret[0][i] = ret[0][i-1]+data[0][i]

for i in range(1,M):
    for j in range(1,M):
        ret[i][j] = min(ret[i-1][j],ret[i][j-1])+data[i][j]

# loop
while True:
    num_change = 0
    # right
    for i in range(M):
        for j in range(1,M):
            if ret[i][j]>ret[i][j-1]+data[i][j]:
                num_change+=1
                ret[i][j]=ret[i][j-1]+data[i][j]
    # down
    for i in range(1,M):
        for j in range(M):
            if ret[i][j]>ret[i-1][j]+data[i][j]:
                num_change+=1
                ret[i][j]=ret[i-1][j]+data[i][j]
    # left
    for i in range(M):
        for j in range(M-1):
            if i==0 and j==0 or i==M-1 and j==M-2:
                continue
            if ret[i][j]>ret[i][j+1]+data[i][j]:
                num_change+=1
                ret[i][j]=ret[i][j+1]+data[i][j]
    # up
    for i in range(M-1):
        for j in range(M):
            if i==0 and j==0 and i==M-1 and j==M-1:
                continue
            if ret[i][j]>ret[i+1][j]+data[i][j]:
                num_change+=1
                ret[i][j]=ret[i+1][j]+data[i][j]
    if num_change==0:
        break

print ret[M-1][M-1]
