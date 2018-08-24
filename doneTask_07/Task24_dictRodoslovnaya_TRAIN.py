import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
myDictReb = {}
myDictRod = {}
listA = []
k = 0
dic2 = {}


def rodo(dic1, p1):
    for j in dic1:
        if p1 == dic1[j]:
            dic2[p1] = {rodo(dic1, j)}
            for i in dic2[p1]:
                dic2[p1][i] = rodo(dic1, i)
            # dic2[p1] = rodo(dic1, j)
            # listA.append(rodo(dic1, j))
            # dic2[p1] = listA
    print(dic2)

for line in inFile:
    f = list(line.strip().split())
    if k < 1:
        n = int(f[0])
        k += 1
    elif k <= n:
        reb, rod = f
        if rod not in myDictRod:
            myDictRod[rod] = reb
        else:
            myDictRod[rod] = [myDictRod.get(rod), reb]
        myDictReb[reb] = rod
p1 = 'Elizabeth'
rodo(myDictReb, p1)
# print(myDictRod)
# print(myDict)
# print(*myDict['Peter_I'])
inFile.close()
outFile.close()
