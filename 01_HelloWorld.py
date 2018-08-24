######################
# SORT  SORTED
######################

myList = list(map(int, input().split()))
myList.sort()
print(' '.join(map(str, myList)))

####################################
myList = list(map(int, input().split()))
sortedList = sorted(myList)
print(' '.join(map(str, sortedList)))
##########
print(sorted((1, 3, 2)))
print(sorted(range(10, -1, -2)))
print(sorted("cba"))

############################################
# Count & SORT
############################################
# отсортировать оценки от 0 до 10

marks = map(int, input().split())
cntMarks = [0] * 11
for mark in marks:
    cntMarks[mark] += 1
for nowMark in range(11):
    print((str(nowMark) + ' ') * cntMarks[nowMark], end='')

##########################################################

a = list(map(int, (input().split())))
newList = []
for i in range(len(a)):
    newList.append((a[i], i))
newList.sort()
print(newList)

#################################################
#             KEY
#################################################

p = [(172, 'Vasya'),
     (180, 'Petya'),
     (172, 'Fedor')
]
def makeT(xyi):
    return (-xyi[0], xyi[1])
p.sort(key=makeT)
print(*p)

#################################################
n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print('\n'.join(sorted(strings, key=len)))

#################################################
# задачу о сортировке точек на плоскости,
# #заданных парой целых координат x и y по неубыванию расстояния от начала координат

def dist(point):
    return point[0] ** 2 + point[1] ** 2

n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=dist)
for point in points:
    print(' '.join(map(str, point)))

#################################################


#################################################
# CLASS
#################################################
class Man:
    height = 0
    name = ''


def manKey(man):
    return (-man.height, man.name)


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[0])
    man.name = tempManData[1]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.height, man.name)
print(*peopleList)

############################################################
# Запись лямбда-функции, возводящей число в квадрат
lambda x: x**2
#эквивалентно
def sqr(x):
    return x**2

############################################################
# с помощью лямбда-функции мы можем вывести список квадратов всех чисел от 1 до 100
print(' '.join(map(lambda x: str(x**2), range(1, 101))))

###########################################################
#сортировки точек по удаленности от начала координат с использованием лямбда-функции
n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=lambda point: point[0]**2 + point[1]**2)
for point in points:
    print(' '.join(map(str, point)))

############################################################
# две записи функции возведения в квадрат эквивалентны
def traditionalSqr(x):
    return x**2
### эквивалентны
lambdaSqr = lambda x: x**2
print(traditionalSqr(3))
print(lambdaSqr(3))

############################################################
#Функции, которые принимают именованные параметры. Например,
# напишем функцию, печатающую что угодно итерируемое, состоящее из чего угодно
# приводимого к строке, с именованным параметром sep, по-умолчанию равным пробелу:

def printList(myList, sep=' '):
    print(sep.join(map(str, myList)))

printList([1, 2, 3])
printList([3, 2, 1], sep='\n')

###########################################################
# функция подсчета суммы всех переданных параметров

def mySum(*args):
    nowSum = 0
    for now in args:
        nowSum += now
    return nowSum

print(mySum(1, 2))
print(mySum(1, 2, 3, 4))

############################################################
# функции, которые принимают не менее определенного количества параметров.
#  Например, мы можем написать функцию поиска минимума среди неопределенного числа аргументов,
#  но в нее должно быть передано не менее одного аргумента

def myMin(first, *others):
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin

print(myMin(1))
print(myMin(3, 1, 2))

#############################################################
#             FILE
#############################################################
inFile = open('input.txt', 'r', encoding='utf8')
a = inFile.readline()      # считывает в переменную первую строку файла
b = inFile.readline()      # считывает вторую строку с этого же файла

# или считать целые числа
a = int(inFile.readline())

# считывам все строки в список. один элемент равен строке включая символ перенос строки
a = inFile.readline()
print([a[0].strip(), a[1].strip()])     # strip() обрезает пробельные символы в начале и конце строки
inFile.readlines() # читает строки и помещает их в список.

# считывет файл в одну строку
s = inFile.read()
print([s])      # только так будет в одной строку с символами перевода строк

##################################
#Расммотрим простой пример: считать все строки файла input.txt и вывести каждую строку развернутой в файл output.txt:

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
for line in lines:
    print(line[-2::-1], file=outFile)
inFile.close()
outFile.close()

##############################################################
# Решение без запоминания всего файла можно было реализовать так:

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    print(line[-2::-1], file=outFile)
inFile.close()
outFile.close()

#######################################################
#            SET
###################################
# Создания множеств
mySet = {3, 1, 2}
print(mySet)

# Сравнения
firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)

# Принимает что угодно иттерируемое
setFromList = set([1, 2, 3])
print(setFromList)
setFromTuple = set((4, 5, 6))
print(setFromTuple)
setFromStr = set("lol")
print(setFromStr)
setFromRange = set(range(2, 22, 3))
print(setFromRange)
setFromMap = set(map(abs, (1, 2, 3, -2, -4)))
print(setFromMap)
setFromSet = set({1, 2, 3})
print(setFromSet)

# Могут содержать различные типы
mixedSet = {1, 3.14, (1, 2, 3), "i have no idea why i'm here"}
print(mixedSet)

# Сортировка множества
mySet = {'abba', 'a', 'long string'}
print(', '.join(mySet))
print(', '.join(sorted(mySet)))
# или
print(sorted(list(mySet)))      # в список и сортировка

# Frozen Set
mixedSet = {1, 3.14, (1, 2, 3), frozenset{(1, 2)}}
print(mixedSet)
print(frozenset(mixedSet))

# Подсчет букв в строке
mySet = set('abbacdddccchhhnnmlmmvfnl')
print(mySet)
print(len(mySet))

# создать пустое множество
emptySet = set()

# Перебрать элементы множества
mySet = {1, '2', 2, '1'}
for elem in mySet:
    print(elem, end=' ')

# проверить, входит ли элемент X в множество A достаточно написать X in A.
# Результатом этой операции будет True или False.
# Чтобы проверить, что элемент не лежит в множестве можно писать not X in A,
# или, более по-человечески X not in A.

mySet = {1, 2, 3}
if 1 in mySet:
    print('1 in set')
else:
    print('1 not in set')
x = 42
if x not in mySet:
    print('x not in set')
else:
    print('x in set')

# Добавление елемента во множество
mySet.add(17)

# Удаление элемента
mySet.remove(17)        # если элемента нет во множестве выдаст ошибку
mySet.discard(17)       # ошибки не будет, просто ничего не сделает

# Сравнение множеств
a = {1, 2, 3, 4}
b = {1, 3}
print(a == b)       # False - Все элементы совпадают
print(a != b)       # Есть различные элементы
print(a < b)        # False - а содержит элементы b и еще чего-т. Все элементы b входят в а
print(a > b)        # True
print(a <= b)       # False
print(a >= b)       # True

# Объединение множеств
print(a | b)        # Объединение множеств
print(a & b)        # Пересечение множеств
print(a - b)        # Множество, элементы которого входят в A, но не входят в B --- LEFT JOIN
print(a ^ b)        # Элементы входят в A | B, но не входят в A & B  -----

########################################
#   Чтение файла
########################################

f = open('input.txt', encoding='utf8')
n = set(range(1, int(f.readline()) + 1))
while True:
    a = f.readline().split()

######################################################
#       DICTIONARY  СЛОВАРЬ
######################################################
# Создание словаря
countries = {'Russia' : 'Europe', 'Germany' : 'Europe', 'Australia' : 'Australia'}

# Создать и добавлять элементы
sqrs = {}
sqrs[1] = 1
sqrs[2] = 4
sqrs[10] = 100
print(sqrs)

# Создание из других объктов
myDict = dict([['key1', 'value1'], ('key2', 'value2')])
print(myDict)

# Узнать по ключу. Если такого ключа в словаре нет, то возникнет ошибка.
phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
print(phones['police'])

# Удаление єлемента словаря
phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
del phones['police']
print(phones)

# Проверка принадлежности ключа словарю осуществляется с помощью операции key in dictionary
# (точно также, как проверка принадлежности элемента множеству).
# Словарь является iterable и возвращает ключи в случайном порядке.
# Например, такой код напечатает содержимое словаря:
phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
for service in phones:
    print(service, phones[service])

# метод items, который возвращает iterable, содержащий в себе кортежи ключ-значение для всевозможных ключей
phones = {'police' : 102, 'ambulance' : 103, 'firefighters' : 101}
for service, phone in phones.items():
    print(service, phone)

# Метод get - принимает два параметра:
# ключ для которого нужно вернуть значения и значение, которое будет возвращено, если такого ключа нет
# Например, подсчитать сколько раз входит в последовательность каждое из чисел:
seq = map(int, input().split())
countDict = {}
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
for key in sorted(countDict):
    print(key, countDict[key], sep = ' : ')

# пример про бензин
s = input()
gasCost = {}
a92, a95, a98 = map(int, input().split())
gasCost[92] = a92
gasCost[95] = a95
gasCost[98] = a98
for i in range(n - 1):
    a92, a95, a98 = map(int, input().split())
    gasCost[92] = min(a92, gasCost[92])
    gasCost[95] = min(a95, gasCost[95])
    gasCost[98] = min(a98, gasCost[98])
print(gasCost[92], gasCost[95], gasCost[98])

# ил красиво
n = int(input())
gasCost = {}
costs = list(map(int, input().split()))
btypes = (92, 95, 98)
for now in range(len(btypes)):
    gasCost[btypes[now]] = costs[now]
for i in range(n - 1):
    costs = list(map(int, input().split()))
    for now in range(len(btypes)):
        gasCost[btypes[now]] = min(costs[now], gasCost[btypes[now]])
print(gasCost[92], gasCost[95], gasCost[98])

####### Использование Словаря в обратном порядке и вывод сортировки
fin = open('input.txt')
myDict = {}
for line in fin:
    eng, latins = line.split('-')
    latinsList = latins.split(',')
    eng = eng.strip()
    for latin in latinsList:
        if latin.strip() not in myDict:
            myDict[latin.strip()] = []
        myDict[latin.strip()].append(eng)
for latin in sorted(myDict):
    print(latin, '-', ', '.join(sorted(myDict[latin])))
################################
n = int(input())
latinEnglish = {}
for i in range(n):
    line = input()
    english = line[:line.find('-')].strip()
    latinsStr = line[line.find('-') + 1:].strip()
    latins = map(lambda s : s.strip(), latinsStr.split(','))
    for latin in latins:
        if latin not in latinEnglish:
            latinEnglish[latin] = []
        latinEnglish[latin].append(english)
print(len(latinEnglish))
for latin in sorted(latinEnglish):
    print(latin, '-', ', '.join(sorted(latinEnglish[latin])))

######################################


#################################################
#   Функциональное программирование
################################################

# filter(predicate, iterable)- применяет функцию predicate ко всем элементам iterable
# и возврщает iterable, который содержит только те элементы, которые удовлетворяли предикаты
# (т.е. функция predicate вернула True).
# Например, так может выглядеть решение задачи о поиске минимального положительного элемента в списке:
print(min(filter(lambda x: x > 0, map(int, input().split()))))

# enumerate - возвращает кортежи из номера элемента (при нумерации с нуля) и значения очередного элемента.
#  С помощью enumerate, например, удобно перебирать элементы iterable (доступ по индексу в которых невозможен)
#  и выводить номера элементов, которые обладают некоторым свойством:
f = open('data.txt', 'r', encoding='utf8')
for i, line in enumerate(f):
    if line.strip() == '':
        print('Blank line at line', i)

# any, all - возвращают истину, если хотя бы один или все элементы iterable истинны соответствнно.
# Например, так можно проверить, не превышают ли все члены последовательности 100 по модулю:
print(all(map(lambda x: abs(int(x)) <= 100, input().split())))

# zip(iterA, iterB, ...) - конструирует кортежи из элементов (iterA[0], iterB[0], ...), (iterA[1], iterB[1], ...), ...


############################################
# библиотека itertools
#############################################################
# itertools.combinations(iterable, size) - генерирует все подмножества множества iterable размером size в виде кортежей.
# Это может быть использовано вместо вложенных циклов при организации перебора.
# Например, мы можем неэффективно решить задачу о поиске трех чисел в последовательности, дающих наибольшее произведение:

from itertools import combinations

nums = list(map(int, input().split()))
combs = combinations(range(len(nums)), 3)
print(max(map(lambda x: nums[x[0]] * nums[x[1]] * nums[x[2]], combs)))

# combinations_with_replacement - могут быть замены


# itertools.permutations(iterable) - генерирует все перестановки iterable.
# Существует вариант функции с двумя параметрами, второй параметр является размером подмножества.
# Тогда генерируются все перестановки всех подмножеств заданного размера.

# itertools.combinations_with_replacement(iterable, size) -
# генерирует все подмножества iterable размером size с повторениями,
#  т.е. одно и то же число можно входить в подмножество несколько раз.

#########################################################
# Модуль functools
#####################################################

# functools.partial предназначена для оберачивания существующих функций с подстановкой некоторых параметров
# функцию-обёртку, преобразующую строки из 0 и 1 в числа
from functools import partial

binStrToInt = partial(int, base=2)
print(binStrToInt('10010'))

printEND = partial(print, end=' ')      # обернули функцию print = чем = постоянным end = ' '

# functools.reduce(func, iterable) позволяет применить функцию ко всем элементам последовательности,
#  используя в качестве первого аргумента накопленный результат.
# Например, если в последовательности были элементы myList = [A, B, C],
# то результатом применения reduce(f, myList) будет f(f(A, B), C).
# С помощью reduce, например, можно найти НОД всех чисел в iterable:

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(reduce(gcd, map(int, input().split())))

# itertools.accumulate(iterable, [func]), которая возвращает iterable со всеми промежуточными значениями,
#  т.е. для списка [A, B, C] accumulate вернет значения A, f(A, B), f(f(A, B), C).
# Например, можно узнать максимальный элемент для каждого префикса (некоторого количества первых элементов)
# заданной последовательности:
from itertools import accumulate

print(*accumulate(map(int, input().split()), max))

#   ЗАДАЧА ТАКСИ
n = int(input())
peopleList = map(int, input().split())
peoples = sorted(list(enumerate(peopleList), key=lambda x: x[1]))
taxiList = map(int, input().split())
taxis = sorted(list(enumerate(taxiList)), key=lambda x: x[1], reverse=True)
ans = sorted(zip(peoples, taxis), key=lambda x: x[0][0])
print(*map(lambda x: x[1][0] + 1, ans))

