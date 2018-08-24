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
    for i in range(len(c)):
        if c[i][2] == j:
            s += c[i][3]
            k += 1
    print(s / k, end=' ')
    # print(s / k, end=' ', file=outFile)
inFile.close()
