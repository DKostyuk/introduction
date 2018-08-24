from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
e = 5 * 10**-7
if abs(d) < 2 * e:
    x = (-b) / (2 * a)
    print(x)
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
