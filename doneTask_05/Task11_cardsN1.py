n = int(input())
s = n
myC = ()
while n - 1 != 0:
    k = int(input())
    myC += (k,)
    n -= 1
for i in range(1, s + 1):
    m = 0
    for j in myC:
        if j == i:
            m += 1
    if m == 0:
        print(i)
