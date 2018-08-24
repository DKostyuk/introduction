a = list(map(int, (input().split())))
a.sort()
i = 0
k = 1
m = 1
b = a[0]
while i < len(a) - 1:
    if a[i] == a[i + 1]:
        k += 1
        c = a[i]
    else:
        k = 1
    if k > m:
        m = k
        b = c
    i += 1
print(b)
