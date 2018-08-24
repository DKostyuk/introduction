s = input()
f = 'h'
pos1 = s.find(f)
pos2 = s.rfind(f)
if s.count(f) <= 2:
    print(s)
else:
    s1 = s[0:pos1+1]
    s2 = s[pos1+1:pos2]
    s3 = s[pos2:]
    s22 = s2.replace(f, 'H')
    print(s1 + s22 + s3)
