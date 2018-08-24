inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
phonesAll = []
s = ''
for line in inFile:
    f = line
    for i in range(len(f)):
        if f[i].isdigit():
            s += f[i]
    if len(s) == 7:
        s = '495' + s
    elif len(s) == 8:
        s = '495' + s[1:]
    elif len(s) == 11:
        s = s[1:]
    phonesAll.append(s)
    s = ''
for i in range(1, len(phonesAll)):
    if len(phonesAll[i]) < 7:
        print('NO')
    else:
        if phonesAll[0] == phonesAll[i]:
            print('YES')
        else:
            print('NO')
inFile.close()
