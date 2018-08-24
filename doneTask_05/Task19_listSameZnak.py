a = list(map(int, (input().split())))
i = 0
n = a[0]
m = 0
while i + 1 < len(a):
    if (a[i + 1] > 0 and a[i] > 0) or (a[i + 1] < 0 and a[i] < 0):
        print(a[i], a[i + 1])
        m += 1
    if m == 1:
        i += len(a)
    else:
        i += 1
