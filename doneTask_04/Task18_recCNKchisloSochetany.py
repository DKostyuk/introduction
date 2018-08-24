def c(n, k):
    if n == k or k == 0 or n == 0:
        return 1
    else:
        f1 = c(n - 1, k)
        f2 = c(n - 1, k - 1)
        return f1 + f2


n = int(input())
k = int(input())
print(c(n, k))
