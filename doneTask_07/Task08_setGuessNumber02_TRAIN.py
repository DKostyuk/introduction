inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
k = 0
for line in inFile:
    f = line.strip()
    if f == 'HELP':
        # e = list(a)
        # e.sort()
        # print(*e)
        print(' '.join(map(str, sorted(a))))
    elif k < 1:
        n = int(f)
        a = set(range(1, n + 1))
        b = a.copy()
        c = a.copy()
        k += 1
    else:
        p = set(map(int, list(f.split())))
        b.difference_update(p)
        c.intersection_update(p)
        # no = a - p
        # yes = a & p
        if len(b) < len(c):
            print('YES')
            a.intersection_update(p)
            b = a.copy()
            c = a.copy()
        else:
            print('NO')
            a.difference_update(p)
            b = a.copy()
            c = a.copy()
inFile.close()
