inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    a = line.split()
    c.append(int(a[-2]))
b = [0] * 100
for i in c:
    b[i] += 1
k = 0
for i in range(len(b)):
    if b[i] == max(b):
        print(i, end=' ', file=outFile)
inFile.close()
outFile.close()
