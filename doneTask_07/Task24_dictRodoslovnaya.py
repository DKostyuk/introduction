import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDict = {}
myDictRod = {}
myDictReb = {}
listA = []
totalV = 0
k = 0
letU = 0
for line in inFile:
    f = list(line.strip().split())
    if k < 1:
        n = int(f[0])
        k += 1
    elif k <= n:
        reb, rod = f
        # if k == 2:
        if rod not in myDictRod and rod not in myDictReb:
            if reb not in myDictReb and reb not in myDictRod:
                myDictRod[rod] = reb
                myDictReb[reb] = rod
            elif reb not in myDictReb and reb in myDictRod:
                myDictRod[rod] = {reb: myDictRod[reb]}
                del myDictRod[reb]
                myDictReb[reb] = rod
        if rod in myDictRod and reb in myDictRod:
            myDictRod[rod] = {myDictRod[rod], myDictRod[reb]}
            del myDictRod[reb]
            myDictReb[reb] = rod
        if rod in myDictRod and reb not in myDictRod:
            myDictRod[rod] = {myDictRod[rod], reb}
            myDictReb[reb] = rod
        if rod not in myDictRod:
            myDictRod[rod] = reb
            myDictReb[reb] = rod
        k += 1
print(myDictRod)
print(myDictReb)
#     elif k == n + 1:
#         for i in range(len(f)):
#             if f[i] not in myDict and f[i].upper() not in myDictU:
#                 for j in f[i]:
#                     if 'A' <= j <= 'Z':
#                         letU += 1
#                         # if j not in ('A', 'E', 'I', 'O', 'U', 'Y'):
#                         #     letU += 1
#                 if letU > 1 or letU == 0:
#                     totalV += 1
#                 letU = 0
#             if f[i] not in myDict and f[i].upper() in myDictU:
#                 totalV += 1
# print(totalV)
inFile.close()
outFile.close()
