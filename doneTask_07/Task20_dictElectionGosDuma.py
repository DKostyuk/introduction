import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
totalV = 0
s = ''
for line in inFile:
    f = list(line.strip().split())
    totalV += int(f[-1])
    for i in range(len(f) - 1):
        s += f[i] + ' '
    s = s.strip()
    myDict[s] = int(f[-1])
    s = ''
tr = totalV / 450
sumM = 0
for it in myDict:
    tt = myDict[it] // tr
    t1 = myDict[it] % tr
    myDict[it] = tt
    listA.append((-t1, it))
    sumM += tt
listA.sort()
n = 0
while sumM < 450:
    myDict[listA[n][1]] = myDict[listA[n][1]] + 1
    sumM += 1
    n += 1
for ir in myDict:
    print(ir, int(myDict[ir]), file=outFile)
inFile.close()
outFile.close()
