inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
t = []
c = []
d = []
for line in inFile:
    a = line.split()
    c.append(a)
for i in range(len(c[0])):
    d.append(int(c[0][i]))
    t.append(int(c[1][i]))
d.sort()
t.sort(reverse=True)
sumM = 0
for i in range(len(d)):
    sumM += d[i] * t[i]
print(sumM, file=outFile)
inFile.close()
outFile.close()
