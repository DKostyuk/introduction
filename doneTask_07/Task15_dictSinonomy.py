inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
myDict1 = {}
myDict2 = {}
k = 0
for line in inFile:
    f = line.strip()
    if k < 1:
        n = int(f)
        k += 1
    elif k <= n:
        listSin = f.split()
        if listSin[0] not in myDict1:
            myDict1[listSin[0]] = []
            myDict1[listSin[0]].append(listSin[1])
        if listSin[1] not in myDict2:
            myDict2[listSin[1]] = []
            myDict2[listSin[1]].append(listSin[0])
        k += 1
    else:
        query = f
        if query in myDict1:
            print(*myDict1[query])
        elif query in myDict2:
            print(*myDict2[query])
inFile.close()
