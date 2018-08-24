def IsPointInArea(x, y):
    a = (((x + 1)**2 + (y - 1)**2) <= 2**2 and y >= 2 * x + 2 and y >= -x) or \
        (((x + 1) ** 2 + (y - 1)**2) >= 2**2 and y <= 2 * x + 2 and y <= -x)
    return a


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
