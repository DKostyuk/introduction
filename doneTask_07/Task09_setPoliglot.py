inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
k = 0
c = []
u = 1
i = 1
allL = set()
uniqL = set()
cAll = []
for line in inFile:
    f = line.strip()
    # c.append(f)
    if k < 1:
        n = int(f)
        a = set(range(1, n + 1))
        k += 1
    elif u == 1:
        m = int(f)
        u = 0
    else:
        if i <= m:
            p = set(list(f.split()))
            allL.update(p)
            b = p.copy()
            # uniqL = b - p
            c.append(f)
            # print(c)
            i += 1
        if i > m:
            cAll.append(tuple(c))
            c = []
            i = 1
            u = 1
t1 = set(cAll[0])
for i in range(1, len(cAll)):
    t1.intersection_update(set(cAll[i]))
print(len(t1))
for i in range(len(t1)):
    print((list(t1))[i])
print(len(allL))
for i in range(len(allL)):
    print((list(allL))[i])
inFile.close()
