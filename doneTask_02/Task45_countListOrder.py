n2 = int(input())
n1 = 0
countMax1 = 1
countMax2 = 1
while n2 != 0:
    if n2 == n1:
        countMax1 += 1
    else:
        if countMax1 >= countMax2:
            countMax2 = countMax1
        countMax1 = 1
    if countMax1 >= countMax2:
        countMax2 = countMax1
    n1 = n2
    n2 = int(input())
print(countMax2)
