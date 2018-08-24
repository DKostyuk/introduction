def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)


n = int(input())
x = 1
y = 3
move(n, x, y)
