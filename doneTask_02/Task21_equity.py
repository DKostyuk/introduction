a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0 and c == 0 and d != 0:
    print('INF')
elif a == 0 and b == 0 and c != 0 and d == 0:
    print('INF')
elif a == 0 and b == 0 and c != 0 and d != 0:
    print('INF')

elif a != 0 and b != 0 and c == 0 and d != 0:
    if -b % a == 0:
        print(-b // a)
    else:
        print('NO')
elif a != 0 and b != 0 and c != 0 and d == 0:
    if -b % a == 0:
        print(-b // a)
    else:
        print('NO')
elif a != 0 and b != 0 and c != 0 and d != 0:
    if -b // a == -d // c:
        print('NO')
    else:
        if -b % a == 0:
            print(-b // a)
        else:
            print('NO')

elif a != 0 and b == 0 and c == 0 and d != 0:
    if -b % a == 0:
        print(-b // a)
    else:
        print('NO')
elif a != 0 and b == 0 and c != 0 and d == 0:
    print('NO')
elif a != 0 and b == 0 and c != 0 and d != 0:
    if -b % a == 0:
        print(-b // a)
    else:
        print('NO')

elif a == 0 and b != 0 and c == 0 and d != 0:
    print('NO')
elif a == 0 and b != 0 and c != 0 and d == 0:
    print('NO')
elif a == 0 and b != 0 and c != 0 and d != 0:
    print('NO')
