import sys
# inFile = open(sys.stdin, 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
p = []
c = []
a = set()
b = set()
# f = sys.stdin.read()
# for line in sys.stdin:
#     print(line.rstrip())
for line in sys.stdin:
        c = line.split()
        for i in range(len(c)):
            a.add(c[i].strip())
# print(a)
print(len(a))
