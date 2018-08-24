def IsPointInCircle(x, y, xc, yc, r):
    a = ((x - xc)**2 + (y - yc)**2) <= r**2
    return a

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
