a = list(map(int, (input().split())))
i = 0
n = a[0]
m = 0
while i + 1 < len(a):
    if a[i + 1] >= a[i] and a[i + 1] >= n:
        n = a[i + 1]
        m = i + 1
    i += 1
print(n, m)
