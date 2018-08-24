from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
e = 2 * 5 * 10**-7
if abs(a) < e and abs(b) < e and abs(c) < e:
    print(3)
elif abs(a) < e and abs(b) < e and c != 0:
    print(0)
elif abs(a) < e and b != 0 and c != 0:
    x = -c / b
    print(1, x)
elif abs(a) < e and b != 0 and abs(c) < e:
    print(1, 0)
else:
    if abs(d) < 2 * e:
        x = (-b) / (2 * a)
        print(1, x)
    elif d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    else:
        print(0)
