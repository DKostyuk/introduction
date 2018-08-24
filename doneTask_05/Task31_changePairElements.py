a = list(map(int, (input().split())))
i = 0
while i <= len(a) - 2:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
print(*a)
