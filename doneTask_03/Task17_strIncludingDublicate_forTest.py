s = input()
a = s[::-1]
f = 'h'
pos1 = s.find(f)
pos2 = len(a) - 1 - a.find(f)
s1 = s[pos1+1:pos2]
s1 = s[0:pos2]
s2 = s[pos1+1:]
print(s1 + s2)
