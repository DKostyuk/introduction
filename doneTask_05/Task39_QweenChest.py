n = 1
b = []
a = []
while n <= 8:
    c = list(map(int, (input().split())))
    a.append(c[0])
    b.append(c[1])
    n += 1
k = 0
for i in range(len(a)):
    for j in range(0, 8):
        if i != j:
            if (a[i] == a[j] or b[i] == b[j] or
                    abs(a[i] - a[j]) == abs(b[i] - b[j])):
                k += 1
if k == 0:
    print('NO')
else:
    print('YES')
