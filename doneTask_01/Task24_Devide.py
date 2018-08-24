a = int(input())
b = int(input())
c = a % b
d = ((c+b-1) // b)
print('YES'*abs(d-1) + 'NO'*d)
