print('С начала суток  прошло N секунд. Введите натуральное число N:')
n = int(input())
secTotal = n % 86400
hours = secTotal // 3600
secMinutes = secTotal % 3600
minutes = secMinutes // 60
seconds = secMinutes % 60
min2 = minutes // 10
sec2 = seconds // 10
print(hours, ':', min2, minutes % 10, ':', sec2, seconds % 10, sep='')
