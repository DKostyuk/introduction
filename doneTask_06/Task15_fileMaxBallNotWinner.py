inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    a = line.split()
    c.append((int(a[2]), int(a[3])))
# print(c)
for j in range(9, 12):
    k = 0
    s = 0
    f = []
    for i in range(len(c)):
        if c[i][0] == j:
            f.append(c[i][1])
    f.sort()
    print(f[f.index(max(f)) - 1], end=' ', file=outFile)
inFile.close()
outFile.close()
