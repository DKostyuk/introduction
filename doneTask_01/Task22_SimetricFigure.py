print('Дано четырехзначное число. Определите, является ли его десятичная запись симметричной.')
print('Если число симметричное, то выведите 1, иначе выведите любое другое целое число.')
print('Число может иметь меньше четырех знаков, тогда нужно считать,')
print('что его десятичная запись дополняется слева незначащими нулями.')
h = int(input())
a4 = h % 10
a3 = (h // 10) % 10
a1a2 = (h // 100)
a4a3 = int(str(a4) + str(a3))
answer = (a1a2 - a4a3) + 1
print(answer)
