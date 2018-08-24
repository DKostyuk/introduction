a = list(map(int, (input().split())))
i = 0
n = a[0]
m = 0
while i + 1 < len(a):
    if a[i + 1] > a[i]:
        print(a[i + 1], end=' ')
    i += 1
