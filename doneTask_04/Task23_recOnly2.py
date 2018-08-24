def only2():
    global kn
    n = int(input())
    n1 = int(n ** 0.5)
    if n != 0:
        if n1**2 == n:
            kn += 1
        only2()
        if n1**2 == n:
            print(n)
    return kn


kn = 0
only2()
if kn == 0:
    print(0)
