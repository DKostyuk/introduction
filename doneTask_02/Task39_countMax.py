n = int(input())
max1 = n
countMax = 0
while n != 0:
    if max1 < n:
        max1 = n
        countMax = 1
    elif max1 == n:
        countMax += 1
    n = int(input())
print(countMax)
