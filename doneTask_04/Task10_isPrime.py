def IsPrime(n):
    if n == 1:
        return False
    i = 2
    c = 0
    while ((i - n**0.5) < 10**-6 or i <= n**0.5) and c != 2:
        if n % i == 0:
            c += 1
        # print('i', i, 'c', c)
        i += 1
    if c >= 1:
        return False
    else:
        return True


b = int(input())
if IsPrime(b):
    print('YES')
else:
    print('NO')
