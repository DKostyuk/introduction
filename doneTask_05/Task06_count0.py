n = int(input())
c = 0
while n != 0:
    k = float(input())
    if k == 0:
        c += 1
    n -= 1
print(c)
