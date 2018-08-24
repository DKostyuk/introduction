inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    c.append(line.strip())
p = list(map(int, c[0].split()))
if p[0] <= p[1]:
    bus1 = set(range(p[0], p[1] + 1))
else:
    bus1 = set(range(p[1], p[0] + 1))
if p[2] <= p[3]:
    bus2 = set(range(p[2], p[3] + 1))
else:
    bus2 = set(range(p[3], p[2] + 1))
print(len(bus1 & bus2))
inFile.close()
