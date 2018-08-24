n = int(input())
n1 = 10**(n-1)
n2 = 10**n - 1
for i in range(n2, n1 - 1, -1):
    if i % 2 != 0:
        print(i, end=' ')
