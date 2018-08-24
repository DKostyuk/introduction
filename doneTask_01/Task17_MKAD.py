print('Введите скорость и время езды:')
v = int(input())
t = int(input())
a = 109
point = (v * t) % a
print(point)
