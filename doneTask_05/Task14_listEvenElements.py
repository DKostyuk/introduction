a = list(map(int, (input().split())))
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        print(a[i])
    i += 1
