a = list(map(int, (input().split())))
i = 0
j = 0
n0 = a.count(0)
while i < len(a):
    if a[i] != 0:
        a[j] = a[i]
        j += 1
    i += 1
a = a[:j] + [0] * n0
print(*a)
