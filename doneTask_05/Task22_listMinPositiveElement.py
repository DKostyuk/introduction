a = list(map(int, (input().split())))
i = 0
n = 1001
while i <= len(a) - 1:
    if a[i] > 0:
        if a[i] < n:
            n = a[i]
    i += 1
print(n)
