inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
k = 0
for line in inFile:
    f = line.strip()
    if f == 'HELP':
        print(*sorted(list(a)), file=outFile)
    elif k < 1:
        n = int(f)
        a = set(range(1, n + 1))
        k += 1
    else:
        p = set(map(int, list(f.split())))
        # no = a - p
        # yes = a & p
        if len(p) == 0.5 * len(a):
            print('NO', file=outFile)
            a.difference_update(p)
        elif 0.5 * len(a) < len(a & p):
            print('YES', file=outFile)
            a.intersection_update(p)
        else:
            print('NO', file=outFile)
            a.difference_update(p)
inFile.close()
outFile.close()
