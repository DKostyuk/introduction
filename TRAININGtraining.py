import datetime
q = 'Dmytro Kostyuk Kosta'
l = '_'.join(q.split())
print('llll  ', l)
now = '-'.join(('_'.join(str(datetime.datetime.now()).split(sep=' '))).split(sep=':'))
now1 = 'Dmytro_Kostyuk_+_+'+'+_+'+now
t = now1.rfind('++++')

print(t)
print(type(t))
print(now1)
print(now1[:(t)])
print(now1[:-1])
print(type(now1))
