p = int(input())
x = int(input())
y = int(input())
z = x * 100 + y
s = z + z * p / 100
x1 = int(s // 100)
y1 = int(s % 100)
print(x1, y1)
