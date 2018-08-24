a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
dm = a * d - c * b
dx = e * d - b * f
dy = a * f - c * e
x = dx / dm
y = dy / dm
print(x, y)
