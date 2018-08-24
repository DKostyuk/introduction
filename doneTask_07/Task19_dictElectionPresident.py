import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
totalV = 0
for line in inFile:
    f = line.strip()
    totalV += 1
    myDict[f] = myDict.get(f, 0) + 1
for it in myDict:
    listA.append((-myDict[it] / totalV, it))
listA.sort()
if listA[0][0] < -0.5:
    print(listA[0][1], file=outFile)
else:
    print(listA[0][1], file=outFile)
    print(listA[1][1], file=outFile)
inFile.close()
outFile.close()
