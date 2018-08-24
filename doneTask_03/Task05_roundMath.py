import math as m
n = float(input())
s = n - (float(m.floor(n)))
e = 5 * 10**-7
# k = float('{0:.2f}'.format(s))
if abs(s - 0.5) < 2 * e:
    print(round(n + 0.1))
else:
    print(round(n))
