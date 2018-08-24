s = input()
i = 0
while i < len(s):
    s = s.replace(s[i], "", 1)
    i += 2
print(s)
