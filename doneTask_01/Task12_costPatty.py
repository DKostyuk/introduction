print('Пирожок в столовой стоит A рублей и B копеек.')
print('Введите стоимость пирожка A рублей, B копеек, N кол-во пирожков:')
a = int(input())
b = int(input())
n = int(input())
costKop = a * 100 + b
costTotal = costKop * n
costRubTotal = costTotal // 100
costKopTotal = costTotal % 100
print(costRubTotal, costKopTotal)
