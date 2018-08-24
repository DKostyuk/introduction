n1 = int(input())
n2 = n1
countBigger = 0
while n2 != 0:
    if n2 > n1:
        countBigger += 1
    n1 = n2
    n2 = int(input())
print(countBigger)
