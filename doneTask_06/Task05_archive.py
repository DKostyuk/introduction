q = list(map(int, (input().split())))
s = q[0]
a = []
for i in range(q[1]):
    c = int(input())
    a.append(c)
    i += 1
a.sort()
k = 0
s1 = 0
i = 0
while i < len(a):
    s1 += a[i]
    if s1 == s:
        k += 1
        i = len(a)
    elif s1 < s:
        k += 1
        i += 1
    elif s1 > s:
        j = 0
        while j < i - 1:
            s1 -= a[j]
            if s1 <= s:
                # k += 1
                j = i
                i = len(a)
            else:
                s1 += a[j]
                j += 1
        i = len(a)
print(k)
