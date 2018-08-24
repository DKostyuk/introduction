a = list(map(int, (input().split())))
for i in range(len(a)):
    k = a.count(a[i])
    if k == 1:
        print(a[i], end=' ')
