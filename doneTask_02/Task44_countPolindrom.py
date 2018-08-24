n = int(input())
i = 1
i2 = 0
b = i
countP = 0
while i <= n:
    while b != 0:
        s = b % 10
        b = b // 10
        i2 = int(str(i2) + str(s))
    if i == i2:
        countP += 1
    i += 1
    b = i
    s = 0
    i2 = 0
print(countP)
