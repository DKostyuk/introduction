h1 = int(input())
v1 = int(input())
h2 = int(input())
v2 = int(input())
if v1 < 1 or v1 > 8 or v2 < 1 or v2 > 8:
    print('NO')
elif h1 < 1 or h1 > 8 or h2 < 1 or h2 > 8:
    print('NO')
else:
    if ((v1 % 2 == 0 and h1 % 2 == 0) or (v1 % 2 == 1 and h1 % 2 == 1)) and \
            ((v2 % 2 == 0 and h2 % 2 == 0) or (v2 % 2 == 1 and h2 % 2 == 1)):
        if v1 < v2:
            if (h1 - (v2 - v1)) <= h2 <= (h1 + (v2 - v1)):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
