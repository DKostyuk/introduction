import math as m
n = float(input())
s = n - (float(m.floor(n)))
r = m.ceil(n - s)
k = int(float('{0:.2f}'.format(s)) * 100)
print(r, k, end=' ')
