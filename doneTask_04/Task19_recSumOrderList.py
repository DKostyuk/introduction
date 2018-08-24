def sumL():
    n = int(input())
    if n == 0:
        return 0
    else:
        s = n + sumL()
    return s


print(sumL())
