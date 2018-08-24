def lang(n):
    if n == 0:
        print(0)
    else:
        n1 = int(n**0.5)
        if n1**2 == n:
            print(int(n1), end=' ')
        else:
            lang(n - (n // n**0.5)**2)
            print(int(n // n**0.5), sep=' ', end=' ')


n = int(input())
lang(n)
