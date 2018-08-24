x = int(input())
y = int(input())
d = 0
z = 0
while z < y:
    z = x
    x = x + x * 0.1
    d = d + 1
print(d)
