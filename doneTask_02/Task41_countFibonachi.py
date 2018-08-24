f = int(input())
sumF = 0
f0 = 1
f1 = 1
countF = 2
if f == 0:
    print(0)
elif f == 1:
    print(1)
elif f == 2:
    print(3)
else:
    while sumF < f:
        sumF = f0 + f1
        f0 = f1
        f1 = sumF
        countF += 1
    if sumF == f:
        print(countF)
    else:
        print(-1)
