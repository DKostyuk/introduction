inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
k = 0
c = []
for line in inFile:
    f = line.strip()
    c.append(f)
    if f == 'HELP':
        e = list(a)
        e.sort()
        print(*e)
    elif k < 1:
        n = int(f)
        a = set(range(1, n + 1))
        k += 1
    elif f != 'YES' and f != 'NO':
        p = set(map(int, list(f.split())))
    elif f == 'YES':
        a.intersection_update(p)
        p = set()
    elif f == 'NO':
        a.difference_update(p)
        p = set()
inFile.close()
