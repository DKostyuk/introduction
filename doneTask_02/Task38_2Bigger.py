n = int(input())
max1 = 0
max2 = 0
while n != 0:
    if max1 <= n:
        max2 = max1
        max1 = n
        # print('if', n, Bigger1, Bigger2)
    else:
        if max2 <= n:
            max2 = n
        # print('else', n, Bigger1, Bigger2)
    n = int(input())
print(max2)
