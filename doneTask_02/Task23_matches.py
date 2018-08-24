l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3
if l1 <= l2 <= l3:
    if l2 <= r1:
        if l3 <= r1 or l3 <= r2:
            print(0)
        else:
            if r2 + d1 >= l3:
                print(1)
            elif r1 + d2 >= l3:
                print(2)
            else:
                print(3)
    else:
        if l3 <= r2:
            print(1)
        else:
            if r2 + d1 >= l3:
                print(1)
            elif r1 + d3 >= l2:
                print(3)
            else:
                print(-1)
if l1 < l3 < l2:
    if l3 <= r1:
        if l2 <= r1 or l2 <= r3:
            print(0)
        else:
            if r3 + d1 >= l2:
                print(1)
            else:
                print(2)
    else:
        if l2 <= r3:
            print(1)
        else:
            if r3 + d1 >= l2:
                print(1)
            elif r1 + d2 >= l2:
                print(2)
            else:
                print(-1)
if l2 < l1 < l3:
    if l1 <= r2:
        if l3 <= r2 or l3 <= r1:
            print(0)
        else:
            if r2 + d1 >= l3:
                print(1)
            elif r1 + d2 >= l3:
                print(2)
            else:
                print(3)
    else:
        if l3 <= r1:
            if r2 + d1 >= l3:
                print(1)
            else:
                print(2)
        else:
            if r1 + d2 >= l3:
                print(2)
            elif r2 + d3 >= l1:
                print(3)
            else:
                print(-1)
if l2 < l3 < l1:
    if l3 <= r2:
        if l1 <= r2 or l1 <= r3:
            print(0)
        else:
            print(1)
    else:
        if l1 <= r3:
            if r2 + d1 >= l3:
                print(1)
            else:
                print(2)
        else:
            if r2 + d1 >= l3:
                print(1)
            if r3 + d2 >= l1:
                print(2)
            else:
                print(-1)
if l3 < l1 < l2:
    if l1 <= r3:
        if l2 <= r3 or l2 <= r1:
            print(0)
        else:
            if r3 + d1 >= l2:
                print(1)
            else:
                print(2)
    else:
        if l2 <= r1:
            if r3 + d1 >= l2:
                print(1)
            elif r3 + d2 >= l1:
                print(2)
            else:
                print(3)
        else:
            if r3 + d2 >= l1:
                print(2)
            elif r1 + d3 >= l2:
                print(3)
            else:
                print(-1)
if l3 < l2 < l1:
    if l2 <= r3:
        if l1 <= r3 or l1 <= r2:
            print(0)
        else:
            print(1)
    else:
        if l1 <= r2:
            if r3 + d1 >= l2:
                print(1)
            elif r3 + d2 >= l1:
                print(2)
            else:
                print(3)
        else:
            if r3 + d1 >= l2:
                print(1)
            elif r2 + d3 >= l1:
                print(3)
            else:
                print(-1)
