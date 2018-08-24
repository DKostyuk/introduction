from math import sqrt
x = int(input())
sumN = 0
sum2 = 0
countN = 0
while x != 0:
    sumN += x
    sum2 += x ** 2
    countN += 1
    x = int(input())
print(sqrt((sum2 - sumN ** 2 / countN) / (countN - 1)))
