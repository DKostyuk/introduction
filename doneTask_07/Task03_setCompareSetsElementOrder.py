a = set(list(map(int, (input().split()))))
b = set(list(map(int, (input().split()))))
print(*sorted(list(a & b)))
