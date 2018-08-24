def cube7(n, k):
    n1 = int(n ** (1 / 3))
    if n1 ** 3 == n:
        print(n1**3, end='')
        return int(n1**3)
    while n1 >= 1:
        s = n1 ** 3
        if k + 1 <= 6:
            s += cube7(n - n1 ** 3, k + 1)
        if s == n:
            print(' ', n1**3, sep='', end='')
            return int(s)
        n1 -= 1
    return 0


n = int(input())
if not cube7(n, 0):
    print(0)
