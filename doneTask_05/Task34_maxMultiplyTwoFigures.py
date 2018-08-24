a = list(map(int, (input().split())))
i = 0
maxX = a[0]
maxX1 = a[0]
minX = a[0]
minX1 = a[0]
while i < len(a) - 1:
    if a[i] == a[i + 1] and a[i + 1] >= maxX:
        maxX1 = maxX
        maxX = a[i]
    elif a[i] == a[i + 1] and maxX1 < a[i + 1] < maxX:
        maxX1 = a[i + 1]

    if a[i] > a[i + 1] and a[i] > maxX:
        maxX1 = maxX
        maxX = a[i]
    elif a[i] > a[i + 1] and maxX1 < a[i] < maxX:
        maxX1 = a[i]
    elif a[i] < a[i + 1] and a[i + 1] > maxX:
        maxX1 = maxX
        maxX = a[i + 1]
    elif a[i] < a[i + 1] and maxX1 < a[i + 1] < maxX:
        maxX1 = a[i + 1]

    elif a[i] < a[i + 1] and a[i] < minX:
        minX1 = minX
        minX = a[i]
    elif a[i] < a[i + 1] and minX1 > a[i] > minX:
        minX1 = a[i]

    elif a[i] > a[i + 1] and a[i + 1] < minX:
        minX1 = minX
        minX = a[i + 1]
    elif a[i] > a[i + 1] and minX1 < a[i + 1] > minX:
        minX1 = minX
        minX = a[i + 1]
    i += 1
if maxX1 * maxX > minX1 * minX:
    print(maxX1, maxX)
else:
    print(minX, minX1)
