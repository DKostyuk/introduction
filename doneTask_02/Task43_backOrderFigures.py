n = int(input())
while n != 0:
    s = n % 10
    n = n // 10
    print(s, end='')
