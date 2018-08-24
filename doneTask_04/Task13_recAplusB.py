def sumAB(a, b):
    if a == 0:
        return b
    return sumAB(a - 1, b + 1)


a = float(input())
b = int(input())
print(sumAB(a, b))
