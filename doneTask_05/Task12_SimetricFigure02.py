a = int(input())
b = int(input())
for h in range(a, b + 1):
    a4 = h % 10
    a3 = (h // 10) % 10
    a1a2 = (h // 100)
    a4a3 = int(str(a4) + str(a3))
    if a1a2 - a4a3 == 0:
        print(h)
