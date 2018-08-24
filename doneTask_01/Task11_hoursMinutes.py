print('С начала суток  прошло N минут. Введите натуральное число N:')
n = int(input())
minTotal = n % 1440
hours = minTotal // 60
minutes = minTotal % 60
print(hours, minutes)
