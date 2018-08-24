import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
totalV = 0
s = ''
for line in inFile:
    f = list(line.strip().split())
    if f[0] == 'DEPOSIT':
        myDict[f[1]] = myDict.get(f[1], 0) + int(f[2])
        #     myDict[f[1]] = 0
        # myDict[f[1]]
    elif f[0] == 'WITHDRAW':
        myDict[f[1]] = myDict.get(f[1], 0) - int(f[2])
    elif f[0] == 'BALANCE':
        if f[1] not in myDict:
            print('ERROR', file=outFile)
        else:
            print(myDict[f[1]], file=outFile)
    elif f[0] == 'TRANSFER':
        myDict[f[1]] = myDict.get(f[1], 0) - int(f[3])
        myDict[f[2]] = myDict.get(f[2], 0) + int(f[3])
    elif f[0] == 'INCOME':
        for it in myDict:
            if myDict[it] > 0:
                myDict[it] = int(myDict.get(it, 0) * (1 + int(f[1]) / 100))
inFile.close()
outFile.close()
