n = int(input())
a = list(map(int, (input().split())))
x = int(input())
k = 2001
i = 0
while i < len(a):
    if abs(a[i] - x) < k:
        k = abs(a[i] - x)
        m = a[i]
    i += 1
print(m)
