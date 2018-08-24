print('Заданы две клетки шахматной доски.')
print('Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.')
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if c1 % 2 != 0 and r1 % 2 != 0:
    k1 = 'B'
elif c1 % 2 == 0 and r1 % 2 == 0:
    k1 = 'B'
else:
    k1 = 'W'
if c2 % 2 != 0 and r2 % 2 != 0:
    k2 = 'B'
elif c2 % 2 == 0 and r2 % 2 == 0:
    k2 = 'B'
else:
    k2 = 'W'
if k1 == k2:
    print('YES')
else:
    print('NO')
