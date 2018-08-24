n = int(input())
k = 0
while k < n:
    for i in range(0, k + 1):
        print(i + 1, end='')
    print()
    k += 1
