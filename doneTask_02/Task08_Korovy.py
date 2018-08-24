print('Для данного числа n<100 закончите фразу “На лугу пасется...”')
print('одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.')
n = int(input())
if 5 <= n <= 20:
    print(n, 'korov')
else:
    if n % 10 == 1:
        print(n, 'korova')
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(n, 'korovy')
    else:
        print(n, 'korov')
