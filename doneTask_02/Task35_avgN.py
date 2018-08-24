n = int(input())
countN = 0
sumN = 0
while n != 0:
    sumN += n
    countN += 1
    n = int(input())
print(sumN / countN)
