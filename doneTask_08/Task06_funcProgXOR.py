# print(map(lambda x, y: x ^ y,
#            ((map, lambda x: int(), map(lambda x: x.split(), (
#     (open('input.txt', 'r', encoding='utf8'))
#         .read().split('\n')))))))

# print(list(map(lambda x: int(x), list(map(lambda x: x.split(), (
#     (open('input.txt', 'r', encoding='utf8'))
#         .read().split('\n')))))))

# print(*map(int, map(str, map(lambda x: x.split('\n'), (open('input.txt', 'r', encoding='utf8')
#         .read())))))


# a = map(int, input().split())
# b = map(int, input().split())
print(*map(lambda x, y: x ^ y, map(int, input().split()), map(int, input().split())))
