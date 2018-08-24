a = list(map(int, (input().split())))
b = a.copy()
max1 = max(a)
a.remove(max1)
max2 = max(a)
min1 = min(b)
b.remove(min1)
min2 = min(b)
if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
