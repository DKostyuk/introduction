def backL():
    n = int(input())
    if n != 0:
        backL()
    print(n)

backL()
