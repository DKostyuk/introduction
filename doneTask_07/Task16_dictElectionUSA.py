inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
myDict1 = {}
for line in inFile:
    listSin = list(line.strip().split())
    if listSin[0] not in myDict1:
        myDict1[listSin[0]] = 0
    myDict1[listSin[0]] = myDict1.get(listSin[0], 0) + int(listSin[1])
for i in sorted(myDict1):
    print(i, myDict1[i])
inFile.close()
