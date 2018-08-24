a = list(map(int, (input().split())))
k = 0
for i in range(len(a)):
    j = i - k
    if a[j] == 0:
        a.append(a.pop(j))
        k += 1
print(*a)
