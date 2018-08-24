print('Введите часы, минуты, секунды для двух моментов времени в пределах одних суток:')
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
secMoment1 = h1*60*60 + m1*60 + s1
secMoment2 = h2*60*60 + m2*60 + s2
diff = secMoment2 - secMoment1
print(diff)
