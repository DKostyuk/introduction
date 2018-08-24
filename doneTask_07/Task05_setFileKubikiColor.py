inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
p = []
c = []
a = set()
b = set()
for line in inFile:
    c.append(line.strip())
p = list(map(int, c[0].split()))
n = p[0]
m = p[1]
for i in range(1, n + 1):
    a.add(int(c[i]))
for i in range(n + 1, len(c)):
    b.add(int(c[i]))
print(len(a & b), file=outFile)
print(*sorted(list(a & b)), file=outFile)
print(len(a - b), file=outFile)
print(*sorted(list(a - b)), file=outFile)
print(len(b - a), file=outFile)
print(*sorted(list(b - a)), file=outFile)
