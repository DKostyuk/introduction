a = list(map(int, (input().split())))
j = 0
k = 0
for i in range(len(a) - 1):
    while j < len(a) - 1:
        if a[i] == a[j + 1]:
            k += 1
        j += 1
    j = i + 1
print(k)
