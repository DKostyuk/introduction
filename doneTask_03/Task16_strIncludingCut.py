s = input()
a = s[::-1]
f = 'h'
pos1 = s.find(f)
pos2 = len(a) - 1 - a.find(f)
s1 = s[0:pos1]
s2 = s[pos2+1:]
print(s1 + s2)
