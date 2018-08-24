def CountSort(a):
    b = [0] * 101
    for i in a:
        b[i] += 1
    for i in range(101):
        print((str(i) + ' ') * b[i], end='')


a = map(int, input().split())
CountSort(a)
