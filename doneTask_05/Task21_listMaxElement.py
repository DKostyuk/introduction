a = list(map(int, (input().split())))
i = 0
n = a[0]
m = 0
while i <= len(a) - 1:
    if a[i] > n:
        n = a[i]
        m = i
    i += 1
print(n, m)
