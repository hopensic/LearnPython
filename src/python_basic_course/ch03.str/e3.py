from math import pi

d = "{num:5}".format(num=1111)
print(d)

a = "{name:10}".format(name="Bob")
# print(a)

e = '{:010.2f}'.format(pi)
print(e)

num = 2.7123432
f = f'num is {num:010.2f}'
print(f)
