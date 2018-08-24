for i in range(0, 1001):
    i1 = i // 10
    i2 = i % 10
    if i == i1 * i2 * 2:
        print(i)
