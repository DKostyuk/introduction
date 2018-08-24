a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
k = 0
for i in range(0, 1001):
    if i - e != 0:
        if (a * i**3 + b * i**2 + c * i + d) / (i - e) == 0:
            k += 1
print(k)
