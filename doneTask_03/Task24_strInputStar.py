s = input()
f = '*'
i = 0
a = ''
if len(s) == 1:
    print(s)
else:
    while i != len(s)-1:
        a += s[i] + f
        i += 1
    print(a + s[len(s) - 1])
