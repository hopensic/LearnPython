from datetime import datetime

'''
tag: ^1281 ^easy
name: ^(Subtract the Product and Sum of Digits of an Integer)
'''


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul, add = 1, 0
        for x in str(n):
            mul *= int(x)
            add += int(x)
        return mul - add


arr1 = 4421

t1 = datetime.now()
s = Solution()
print(s.subtractProductAndSum(arr1))
t2 = datetime.now()
print(t2 - t1)
