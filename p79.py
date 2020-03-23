content = open('p079_keylog.txt').readlines()

d = {}

for line in content:
    s = line.strip()
    d[(s[0],s[1])] = d.get((s[0],s[1]),0)+1
    d[(s[1],s[2])] = d.get((s[1],s[2]),0)+1
    d[(s[0],s[2])] = d.get((s[0],s[2]),0)+1

for k,v in d.iteritems():
    print k,v
