inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
for line in inFile:
    f = list(line.strip().split())
    for i in f:
        myDict[i] = myDict.get(i, 0) + 1
for it in myDict:
    listA.append((-myDict[it], it))
for i in sorted(listA):
    print(i[1])
inFile.close()
