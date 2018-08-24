n = int(input()) + 1
f = 0
f0 = 1
f1 = 1
k = 3
if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    while k != n:
        f = f0 + f1
        f0 = f1
        f1 = f
        k += 1
    print(f)
