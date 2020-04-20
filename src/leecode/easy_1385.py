from datetime import datetime

'''
tag: ^1385 ^easy ^array
name: ^(Find the Distance Value Between Two Arrays)
'''


class Solution:
    def findTheDistanceValue(self, arr1: list, arr2: list, d: int) -> int:
        def fun(x):
            for k in arr2:
                if abs(x - k) <= d:
                    return 0
            return 1

        return sum(map(fun, arr1))


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

t1 = datetime.now()
s = Solution()
print(s.findTheDistanceValue(arr1, arr2, d))
t2 = datetime.now()
print(t2 - t1)
