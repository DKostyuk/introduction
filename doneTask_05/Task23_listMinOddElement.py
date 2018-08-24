a = list(map(int, (input().split())))
i = 0
j = 0
while i <= len(a) - 1:
    if a[i] % 2 != 0:
        n = a[i]
        i = len(a)
    else:
        i += 1
while j <= len(a) - 1:
    if a[j] % 2 != 0:
        if a[j] < n:
            n = a[j]
    j += 1
print(n)
