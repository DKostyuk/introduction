inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    a = line.split()
    a[2] = int(a[2])
    a[3] = int(a[3])
    c.append(a)
for j in range(9, 12):
    k = 0
    s = 0
    f = []
    for i in range(len(c)):
        if c[i][2] == j:
            f.append(c[i][3])
    for i in range(len(c)):
        if c[i][3] == max(f):
            k += 1
    print(k, end='', file=outFile)
            f.append(c[i][3])
    print(max(f), end=' ', file=outFile)
inFile.close()
outFile.close()
