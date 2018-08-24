import io

inFile = io.open('input.txt', 'r', encoding='utf8')
outFile = io.open('output.txt', 'w', encoding='utf8')
myDictRod = {}
k = 0

for line in inFile:
    f = list(line.strip().split())
    if k < 1:
        n = int(f[0])
        k += 1
    elif k <= n:
        reb, rod = f
        if rod not in myDictRod:
            myDictRod[rod] = None
        myDictRod[reb] = rod
for key, value in sorted(myDictRod.items()):
    level = 0
    print(key, end=' ', file=outFile)
    while key in myDictRod:
        level += 1
        key = myDictRod[key]
    print(level - 1, file=outFile)
inFile.close()
outFile.close()
