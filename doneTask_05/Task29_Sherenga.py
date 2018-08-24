a = list(map(int, (input().split())))
x = int(input())
i = 0
while i < len(a):
    if x > a[i]:
        m = i + 1
        i = len(a)
    else:
        m = i + 2
    i += 1
print(m)
