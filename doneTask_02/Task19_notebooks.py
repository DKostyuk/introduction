a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
d1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
d2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
d3 = (a1 // c2) * (b1 // b2) * (c1 // a2)
d4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
d5 = (a1 // b2) * (b1 // a2) * (c1 // c2)
d6 = (a1 // c2) * (b1 // a2) * (c1 // b2)
if d1 >= d2:
    n1 = d1
else:
    n1 = d2
if n1 >= d3:
    n1 = n1
else:
    n1 = d3
if d4 >= d5:
    n2 = d4
else:
    n2 = d5
if n2 >= d6:
    n2 = n2
else:
    n2 = d5
if n1 >= n2:
    print(n1)
else:
    print(n2)
