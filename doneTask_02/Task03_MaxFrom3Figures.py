print('Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число)')
print('Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?')
a = int(input())
b = int(input())
c = int(input())
if a >= b:
    d = a
else:
    d = b
if d >= c:
    print(d)
else:
    print(c)
