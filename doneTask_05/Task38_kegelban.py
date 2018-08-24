q = list(map(int, (input().split())))
a = list(range(1, q[0] + 1))
i = 1
b = []
while i <= q[1]:
    c = list(map(int, (input().split())))
    b.extend(range(c[0], c[1] + 1))
    i += 1
for i in range(len(a)):
    m = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            m += 1
    if m >= 1:
        print('.', end='')
    else:
        print('I', end='')
