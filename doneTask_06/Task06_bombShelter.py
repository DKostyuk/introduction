n = int(input())
a = list(map(int, (input().split())))
m = int(input())
b = list(map(int, (input().split())))
for i in range(len(a)):
    a[i] = (a[i], i + 1)
for i in range(len(b)):
    b[i] = (b[i], i + 1)
a.sort()
b.sort()
c = list([0] * (n + 1))
i = 0
j = 0
while i < len(a) and j < len(b):
    minS = abs(a[i][0] - b[j][0])
    minSi = b[j][1]
    k = j
    while j < len(b):
        if abs(a[i][0] - b[j][0]) == minS:
            j += 1
        elif abs(a[i][0] - b[j][0]) < minS:
            minS = abs(a[i][0] - b[j][0])
            minSi = b[j][1]
            c[a[i][1]] = minSi
            k = j
            j += 1
        elif abs(a[i][0] - b[j][0]) > minS:
            j = len(b)
        c[a[i][1]] = minSi
    j = k
    i += 1
    if j + 1 == len(b):
        for q in range(i, len(a)):
            c[a[q][1]] = b[j][1]
        j = len(b)
print(*c[1:len(c)])
