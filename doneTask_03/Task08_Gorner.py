n = int(input())
x = float(input())
ai = float(input())
bi = ai
i = n
s = 0
if n == 0:
    print(ai)
else:
    while i > 0:
        ai2 = float(input())
        bi1 = ai2 + bi * x
        bi = bi1
        i -= 1
    print(float('{0:.2f}'.format(bi)))
