inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
c = []
for line in inFile:
    a = line.split()
    c.append(a)
k = int(c.pop(0)[0])
for i in range(len(c)):
    c[i] = [(int(c[i][-3]) + int(c[i][-2]) + int(c[i][-1])),
            int(c[i][-3]), int(c[i][-2]), int(c[i][-1])]
# print(c)
# print('k=', k)
f = []
for i in range(len(c)):
    if c[i][1] >= 40 and c[i][2] >= 40 and c[i][3] >= 40:
        f.append(c[i][0])
f.sort(reverse=True)
# print(f)
if k == 0:
    print(1, file=outFile)
elif len(f) == 0:
    print(1, file=outFile)
elif len(f) <= k:
    print(0, file=outFile)
elif len(f) > k:
    w = f[k - 1]
    # print(w)
    firstK = f.index(w)
    # print(firstK)
    if w > f[k]:
        print(w, file=outFile)
    elif firstK == 0 and w == f[k]:
        print(1, file=outFile)
    else:
        ball = f[firstK - 1]
        print(ball, file=outFile)
inFile.close()
outFile.close()
