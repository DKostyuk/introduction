def IsPointInSquare(x, y):
    a = (y <= x + 1) and (y <= 1 - x) and (y >= x - 1) and (y >= -x - 1)
    return a

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
