def distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
d12 = distance(x1, y1, x2, y2)
d13 = distance(x1, y1, x3, y3)
d23 = distance(x2, y2, x3, y3)
print(d12 + d13 + d23)
