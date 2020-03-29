content = open('p082_matrix.txt','r').readlines()

data = []
for line in content:
    line = [int(num) for num in line.strip().split(',')]
    data.append(line)

data = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

NUM = len(data)

ret = [[0 for i in range(NUM)] for j in range(NUM)]

for i in range(NUM):
    ret[i][0] = data[i][0]

for i in range(1,NUM):
    # initialize
    for j in range(NUM):
        ret[j][i] = data[j][i]+ret[j][i-1]
    # loop
    while True:
        change_num = 0
        for j in range(NUM):
            if j==0:
                if ret[0][i]>ret[1][i]+data[0][i]:
                    change_num+=1
                    ret[0][i] = ret[1][i]+data[0][i]
            elif j==NUM-1:
                if ret[NUM-1][i]>ret[NUM-2][i]+data[NUM-1][i]:
                    change_num+=1
                    ret[NUM-1][i] = ret[NUM-2][i]+data[NUM-1][i]
            else: 
                if ret[j][i]>min(ret[j+1][i]+data[j][i],ret[j-1][i]+data[j][i]):
                    change_num+=1
                    ret[j][i] = min(ret[j+1][i]+data[j][i],ret[j-1][i]+data[j][i])
        if change_num==0:
            break

min_value = ret[0][NUM-1]
for i in range(1,NUM):
    if ret[i][NUM-1]<min_value:
        min_value = ret[i][NUM-1]

print min_value


