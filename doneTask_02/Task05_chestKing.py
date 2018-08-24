print('Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.')
print('Даны две различные клетки шахматной доски, определите,')
print('может ли король попасть с первой клетки на вторую одним ходом.')
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if c1 + 1 == c2 and r1 + 1 == r2:
    print('YES')
elif c1 + 1 == c2 and r1 == r2:
    print('YES')
elif c1 + 1 == c2 and r1 - 1 == r2:
    print('YES')
elif c1 - 1 == c2 and r1 + 1 == r2:
    print('YES')
elif c1 - 1 == c2 and r1 == r2:
    print('YES')
elif c1 - 1 == c2 and r1 - 1 == r2:
    print('YES')
elif c1 == c2 and r1 + 1 == r2:
    print('YES')
elif c1 == c2 and r1 - 1 == r2:
    print('YES')
else:
    print('NO')
