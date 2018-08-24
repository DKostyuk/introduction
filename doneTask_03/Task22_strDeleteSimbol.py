s = input()
f = '@'
pos = s.find(f)
s1 = ''
if pos == -1:
    print(s)
else:
    while pos != -1:
        pos = s.find(f)
        if pos != -1:
            s1 = s1 + s[0:pos]
            s = s[pos+1:]
        else:
            s1 = s1 + s[0:]
print(s1)
