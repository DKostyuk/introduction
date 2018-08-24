n2 = int(input())
n1 = n2
countMax1 = 1
countMax2 = 1
countMin1 = 1
countMin2 = 1
while n2 != 0:
    if n2 > n1:
        countMax1 += 1
        # print(countMax1, countMax2)
    else:
        if countMax1 >= countMax2:
            countMax2 = countMax1
        countMax1 = 1
    if countMax1 >= countMax2:
        countMax2 = countMax1
    if n2 < n1:
        countMin1 += 1
    else:
        if countMin1 >= countMin2:
            countMin2 = countMin1
        countMin1 = 1
    if countMin1 >= countMin2:
        countMin2 = countMin1
    n1 = n2
    n2 = int(input())
# print(countMax2)
# print(countMin2)
if countMax2 >= countMin2:
    print(countMax2)
else:
    print(countMin2)
