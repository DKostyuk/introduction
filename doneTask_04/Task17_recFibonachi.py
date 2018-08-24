def phib(n):
    k = 2
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        if k != n:
            f = phib(n-1) + phib(n-2)
            k += 1
        return f


n = int(input())
print(phib(n))
