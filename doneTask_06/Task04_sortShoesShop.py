n = int(input())
a = list(map(int, (input().split())))
a.sort()
k = 0
c = 0
for i in range(len(a)):
    if a[i] >= n and a[i] - c >= 3:
        k += 1
        c = a[i]
    elif a[i] >= n and k == 0:
        k += 1
        c = a[i]
print(k)
