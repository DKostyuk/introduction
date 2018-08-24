a = list(map(str, (input().split())))
k = int(input())
while k <= len(a) - 2:
    a[k] = a[k + 1]
    k += 1
a.pop()
print(' '.join(map(str, a)))
