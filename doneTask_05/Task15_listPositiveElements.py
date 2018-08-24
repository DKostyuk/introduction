a = list(map(int, (input().split())))
i = 0
k = 0
while i < len(a):
    if a[i] > 0:
        k += 1
    i += 1
print(k)
