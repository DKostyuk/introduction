def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input())
sumF = 0
while n != 0:
    sumF += factorial(n)
    n -= 1
print(sumF)
