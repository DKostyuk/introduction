inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
c = []
i = 1
zAll = set()
for line in inFile:
    c.append(line.strip())
p = list(map(int, c[0].split()))
weekend = set(range(6, p[0] + 1, 7)) | set(range(7, p[0] + 1, 7))
while i <= p[1]:
    t = list(map(int, c[i].split()))
    z = set(range(t[0], p[0] + 1, t[1]))
    zAll.update(z)
    i += 1
zAll -= weekend
print(len(zAll))
inFile.close()
