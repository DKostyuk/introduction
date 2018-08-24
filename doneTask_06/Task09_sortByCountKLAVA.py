n = int(input())
a = list(map(int, (input().split())))
k = int(input())
b = list(map(int, (input().split())))
c = [0]*(n + 1)
for i in b:
    c[i] += 1
for i in range(len(a)):
    if a[i] >= c[i + 1]:
        print('NO')
    else:
        print('YES')
