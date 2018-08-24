n = int(input())
countEven = 0
while n != 0:
    if n % 2 == 0:
        countEven += 1
    n = int(input())
print(countEven)
