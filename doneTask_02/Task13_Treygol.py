a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        h3 = a
        h2 = b
        h1 = c
    else:
        h3 = c
        h2 = b
        h1 = a
else:
    if b > c:
        h3 = b
        h2 = c
        h1 = a
    else:
        h3 = c
        h2 = b
        h1 = a
if h1 + h2 > h3:
    if (h1*h1 + h2*h2) == h3*h3:
        print('rectangular')
    elif h3*h3 < (h1*h1 + h2*h2):
        print('acute')
    elif h3*h3 > (h1*h1 + h2*h2):
        print('obtuse')
else:
    print('impossible')
