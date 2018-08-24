p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
s = 0
while i <= k:
    z = x * 100 + y
    s = z + z * p / 100
    x = int(s // 100)
    y = int(s % 100)
    i += 1
print(x, y)
