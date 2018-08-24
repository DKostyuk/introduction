def MinDivisor(n):
    i = 2
    while ((i - n**0.5) < 10**-6 or i <= n**0.5) and n % i != 0:
        i += 1
    if n % i == 0:
        return i
    else:
        return n


n = int(input())
print(MinDivisor(n))
