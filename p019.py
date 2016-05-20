from datetime import datetime,date

cnt = 0

for year in range(1901,2001):
    for month in range(1,13):
        d = datetime(year,month,1)
        if d.weekday() == 6:
            cnt += 1

print cnt
