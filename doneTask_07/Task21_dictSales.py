import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
totalV = 0
s = ''
for line in inFile:
    f = list(line.strip().split())
    if f[0] not in myDict:
        myDict[f[0]] = {}
    if f[1] not in myDict[f[0]]:
        myDict[f[0]][f[1]] = 0
    myDict[f[0]][f[1]] += int(f[2])
for i in sorted(myDict):
    print(i, ':', sep='', file=outFile)
    for s in sorted(myDict[i]):
        print(s, myDict[i][s], file=outFile)
inFile.close()
outFile.close()
