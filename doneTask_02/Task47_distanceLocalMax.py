n1 = int(input())
n2 = n1
n3 = n2
k = 1
lmPrev = 0
kmPrev = 0
d = 0
da = 0
m = 0
while n3 != 0:
    if n1 < n2 > n3:
        d = k - kmPrev
        lmPrev = n2
        kmPrev = k
        m += 1
        if m == 2:
            da = d
        elif m > 2 and d < da:
            da = d
    n1 = n2
    n2 = n3
    k += 1
    n3 = int(input())
print(da)
