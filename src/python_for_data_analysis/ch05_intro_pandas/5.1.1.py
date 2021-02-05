import pandas as pd

obj = pd.Series([2, -3, "4", 1])
# print(obj)
# print(obj.values)
# print(obj.index)


obj2 = pd.Series([2, 1, 3, 4], index=['d', 'b', 'a', 'c'])
print(obj2)
print('-----')
print(obj2.values)
print('-----')
print(obj2.index)
print('-----')
print(obj2['c'])
print(obj2[['c','a','d']])
print(type(obj2[['c','a','d']]))

