inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
p = []
c = []
v = []
a = []
exp = 2 * 5 * 10**-7
for line in inFile:
    c.append(line.strip())
m = c.index('VOTES:')
p = c[1:m]
v = c[m + 1:]
for i in range(len(p)):
    k = v.count(p[i])
    a.append((k, p[i], k / len(v)))
for i in range(len(a)):
    if a[i][2] > 0.07 or abs(a[i][2] - 0.07) < exp:
        print(a[i][1], file=outFile)
inFile.close()
outFile.close()
