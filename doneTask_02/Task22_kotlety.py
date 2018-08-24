k = int(input())
m = int(input())
n = int(input())
if n > k:
    print(((2 * n + k - 1) // k) * m)
else:
    print(2 * m)
