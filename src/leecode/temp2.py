from datetime import datetime

aa = datetime.now()


a = 0


if a:
    print('111')
else:
    print('222')



bb = datetime.now()
print(bb - aa)
