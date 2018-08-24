n = 1
a =[]
b = []
while n <= 8:
    c = list(map(int, (input().split())))
    a.append(c[0])
    b.append(c[1])
    n += 1
k = 0
for j in range(len(a)):
    i = 0
    while i < len(b) - 3:
        if b[i] == b[i + 2]:
            k += 1
        elif abs(b[i] - b[i + 2]) == abs(b[i + 1] - b[i + 3]):
            k += 1
        i += 1
if k == 0:
    print('NO')
else:
    print('YES')
