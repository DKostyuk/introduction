print('Введите в отдельных строках:')
print('целое кол-во школьников(до 10000) и целое кол-во яблок(до 10000)')
pupil_quantity = int(input())
apple_quantity = int(input())
apple_rest = apple_quantity // pupil_quantity
print(apple_rest)
