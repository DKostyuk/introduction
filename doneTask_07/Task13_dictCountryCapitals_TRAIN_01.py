import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
listQ = []
for k, line in enumerate(inFile):
    if k == 0:
        n = int(line.strip())
    elif k in range(1, n + 1):
        listCountry = line.strip().split()
        for i in range(1, len(listCountry)):
            if listCountry[i] not in myDict:
                myDict[listCountry[i]] = []
            myDict[listCountry[i]].append(listCountry[0])
    elif k in range(n + 1, n + 2):
        m = int(line.strip())
    elif k in range(n + 2, n + m + 3):
        listQ.append(line.strip())
for c in listQ:
    for key, value in myDict.items():
        if c in key:
            print(*value, file=outFile)

        # for key, value in myDict.items():
        #     if f in value:
        #         print(key, file=outFile)
inFile.close()
outFile.close()
