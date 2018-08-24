def min4(a, b, c, d):
    s1 = min(a, b)
    s2 = min(c, d)
    s = min(s1, s2)
    return s

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
