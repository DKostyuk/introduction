a = list(map(int, (input().split())))
i = 1
n = a[0]
m = 0
while i <= len(a) - 2:
    if a[i - 1] < a[i] > a[i + 1]:
        m += 1
    i += 1
print(m)
