a = list(map(int, (input().split())))
i = 0
k = 0
while i < len(a) and k < len(a):
    if a[i] == 0:
        a.append(a[i])
        del a[i]
    else:
        i += 1
    k += 1
print(*a)
