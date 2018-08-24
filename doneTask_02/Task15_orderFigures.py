a = int(input())
b = int(input())
c = int(input())
if a >= b:
    (a, b) = (a, b)
else:
    (a, b) = (b, a)
if a >= c and b >= c:
    print(c, b, a)
elif a >= c >= b:
    print(b, c, a)
else:
    print(b, a, c)
