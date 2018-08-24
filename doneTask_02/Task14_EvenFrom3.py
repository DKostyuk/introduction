a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    a1 = 1
else:
    a1 = 0
if b % 2 == 0:
    b1 = 1
else:
    b1 = 0
if c % 2 == 0:
    c1 = 1
else:
    c1 = 0
d = a1 + b1 + c1
if d == 2 or d == 1:
    print('YES')
else:
    print('NO')
