a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
exp = 2 * 5 * 10**-7
dm = a * d - c * b
dx = e * d - b * f
dy = a * f - c * e
if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif (a == 0 and b == 0 and c == 0 and d == 0 and e != 0 and f == 0) or \
        (a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f != 0) or \
        (a == 0 and b == 0 and c == 0 and d == 0 and e != 0 and f != 0):
    print(0)
elif abs(dm) < exp:
    if abs(dx) < exp and abs(dy) < exp:
        if a == 0 and b == 0 and c == 0 and d == 0:
            print(5)
        elif a == 0 and c == 0:
            if b != 0:
                y = e / b
                print(4, y)
            elif d != 0:
                y = f / d
                print(4, y)
            elif b != 0 and d != 0:
                y = e / b
                print(4, y)
        elif b == 0 and d == 0:
            if a != 0:
                x = e / a
                print(3, x)
            elif c != 0:
                x = f / c
                print(3, x)
            elif a != 0 and c != 0:
                x = e / a
                print(3, x)
        elif d != 0:
            p = -c / d
            q = f / d
            print(1, p, q)
        elif b != 0:
            p = -a / b
            q = e / b
            print(1, p, q)
        else:
            p = -c / d
            q = f / d
            print(1, p, q)
    elif abs(dx) > exp or abs(dy) > exp:
        print(0)
else:
    x = dx / dm
    y = dy / dm
    print(2, x, y)
