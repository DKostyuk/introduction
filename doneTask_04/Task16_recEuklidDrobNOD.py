def ReduceFraction(a, b):
    def nod(a, b):
        if b == 0:
            return abs(a)
        else:
            return nod(b, a % b)
    return a // nod(a, b), b // nod(a, b)

a = int(input())
b = int(input())
print(ReduceFraction(a, b)[0], ReduceFraction(a, b)[1])
