def power(a, n):
    s = 1
    if n == 0:
        return 1
    else:
        if n > 0:
            while n != 0:
                s = s * a
                n -= 1
        else:
            while n != 0:
                s = s * a
                n += 1
            s = 1 / s
        return s


a = float(input())
n = int(input())
print(power(a, n))
