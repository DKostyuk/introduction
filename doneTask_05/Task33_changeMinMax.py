a = list(map(int, (input().split())))
i = -1
maxX = a[0]
maxXi = 0
minX = a[0]
minXi = 0
while i < len(a) - 1:
    if a[i] > a[i + 1] and a[i] > maxX:
        maxX = a[i]
        maxXi = i
    elif a[i] < a[i + 1] and a[i + 1] > maxX:
        maxX = a[i + 1]
        maxXi = i + 1
    elif a[i] < a[i + 1] and a[i] < minX:
        minX = a[i]
        minXi = i
    elif a[i] > a[i + 1] and a[i + 1] < minX:
        minX = a[i + 1]
        minXi = i + 1
    i += 1
a[maxXi], a[minXi] = a[minXi], a[maxXi]
print(*a)
