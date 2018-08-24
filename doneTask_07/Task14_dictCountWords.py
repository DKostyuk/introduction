inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
myDict = {}
for line in inFile:
    f = list(line.strip().split())
    for i in f:
        myDict[i] = myDict.get(i, 0) + 1
        print(myDict[i] - 1, end=' ')
inFile.close()
