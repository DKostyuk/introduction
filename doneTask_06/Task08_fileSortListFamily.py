inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    a = line.split()
    a[2] = int(a[2])
    a[3] = int(a[3])
    c.append(a)
c.sort()
for i in range(len(c)):
    print(c[i][0], c[i][1], c[i][3], file=outFile)
inFile.close()
outFile.close()
