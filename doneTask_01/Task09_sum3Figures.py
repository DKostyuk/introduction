print('Введите трехзначное число N:')
n = int(input())
figure01 = (n // 10) // 10
figure02 = (n // 10) % 10
figure03 = n % 10
print(figure01+figure02+figure03)
