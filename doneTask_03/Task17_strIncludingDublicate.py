s = input()
a = s[::-1]
f = 'h'
pos1 = s.find(f)
pos2 = len(a) - 1 - a.find(f)
s1 = s[pos1+1:pos2]
print(s1 * 2)
