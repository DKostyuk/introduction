inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
myDict = {}
listA = []
for line in inFile:
    f = list(line.strip().split())
    for i in f:
        myDict[i] = myDict.get(i, 0) + 1
a = sorted(myDict.items(), key=lambda x: x[1], reverse=True)
i = 0
while i < len(a):
    if a[i][1] == a[0][1]:
        listA.append(a[i][0])
        i += 1
    else:
        i = len(a)
print(sorted(listA)[0])
inFile.close()
