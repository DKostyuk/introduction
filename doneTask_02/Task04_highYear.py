print('Дано натуральное число. Требуется определить, является ли год с данным номером високосным.')
print('Если год является високосным, то выведите YES, иначе выведите NO.')
print('Напомним, что в соответствии с григорианским календарем, год является високосным,')
print('если его номер кратен 4, но не кратен 100, а также если он кратен 400.)')
a = int(input())
if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
    print('NO')
else:
    print('YES')