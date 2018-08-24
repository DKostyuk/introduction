def IsPointInSquare(x, y):
    a = -1 <= x <= 1 and -1 <= y <= 1
    return a

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
