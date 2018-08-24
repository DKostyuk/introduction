import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
k = 0
listQ = []
dictA = {}
for k, line in enumerate(inFile):
    if k == 0:
        n = int(line.strip())
    elif k in range(1, n + 1):
        listCountry = line.strip().split()
        country, *city = listCountry  # * - объединение элементов
        myDict[country] = city
    elif k in range(n + 1, n + 2):
        m = int(line.strip())
    elif k in range(n + 2, n + m + 3):
        f = line.strip()
        listQ.append(f)
for key, value in myDict.items():
    for j in listQ:
        if j in value:
            dictA[j] = key
for j in listQ:
    print(dictA[j], file=outFile)
inFile.close()
outFile.close()
