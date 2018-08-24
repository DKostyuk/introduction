a = list(map(int, (input().split())))
b = list(map(int, (input().split())))
k = b[0]
x = b[1]
a.append(x)
i = -1
n = -(len(a) - k)
# for i in a:
while i >= n:
    if i == n:
        a[i] = x
    else:
        a[i] = a[i - 1]
    i -= 1
print(' '.join(map(str, a)))
