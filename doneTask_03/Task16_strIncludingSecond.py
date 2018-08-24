s = input()
a = s[::-1]
f = 'f'
pos1 = s.find(f)
pos2 = len(a) - 1 - a.find(f)
if 0 <= pos1 < pos2 < len(s):
    print(pos1, pos2)
elif 0 < pos1 < len(s):
    print(pos1)
