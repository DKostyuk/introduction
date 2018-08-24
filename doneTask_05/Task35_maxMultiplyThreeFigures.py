a = list(map(int, (input().split())))
b = a.copy()
if len(a) == 3:
    print(a[0], a[1], a[2])
else:
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    a.remove(max2)
    max3 = max(a)
    min6 = min(b)
    b.remove(min6)
    min5 = min(b)
    b.remove(min5)
    min4 = min(b)
    m123 = max1 * max2 * max3
    m156 = max1 * min5 * min6
    m125 = max1 * max2 * min5
    m126 = max1 * max2 * min6
    if max(m123, m156, m125, m126) == m123:
        print(max1, max2, max3)
    elif max(m123, m156, m125, m126) == m156:
        print(max1, min5, min6)
    elif max(m123, m156, m125, m126) == m125:
        print(max1, max2, min5)
    elif max(m123, m156, m125, m126) == m126:
        print(max1, max2, min6)
