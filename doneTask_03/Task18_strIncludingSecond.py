s = input()
a = s[::-1]
f = 'f'
pos1 = s.find(f)
pos2 = s.find(f, pos1 + 1)
if 0 <= pos1 < pos2 < len(s):
    print(pos2)
elif 0 <= pos1 < len(s):
    print(-1)
elif pos1 == -1:
    print(-2)
