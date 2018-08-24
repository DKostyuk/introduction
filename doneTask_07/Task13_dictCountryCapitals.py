import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
k = 0
listQ = []
for line in inFile:
    f = line.strip()
    if k < 1:
        n = int(f)
        k += 1
    elif k <= n:
        listCountry = f.split()
        for i in range(1, len(listCountry)):
            if listCountry[i] not in myDict:
                myDict[listCountry[i]] = []
            myDict[listCountry[i]].append(listCountry[0])
        k += 1
    elif k == n + 1:
        m = int(f)
        k += 1
    else:
        if f in myDict:
            print(*myDict[f], file=outFile)
inFile.close()
outFile.close()
