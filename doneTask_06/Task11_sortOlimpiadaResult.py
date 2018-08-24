def makeT(x):
    return (-x[1], x[0])


n = int(input())
a = []
c = [0] * n
while n != 0:
    b = tuple(input().split())
    a.append((b[0], int(b[1])))
    n -= 1
a.sort(key=makeT)
for i in range(len(a)):
    print(a[i][0])
