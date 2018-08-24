a = list(map(int, (input().split())))
i = -1
x = a[-1]
while i >= -len(a):
    if i == -len(a):
        a[i] = x
    else:
        a[i] = a[i - 1]
    i -= 1
print(*a)
