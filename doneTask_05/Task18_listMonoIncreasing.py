def IsAscending(a):
    i = 0
    s = True
    while i + 1 < len(a):
        s = s and (a[i + 1] > a[i])
        i += 1
    return s

a = list(map(int, (input().split())))
if IsAscending(a):
    print('YES')
else:
    print('NO')
