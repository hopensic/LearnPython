from datetime import datetime

'''
tag: ^1413 ^easy ^array
name: ^(Minimum Value to Get Positive Step by Step Sum)
'''


class Solution:
    def minStartValue(self, nums: list) -> int:
        minnum = 99999
        sums = 0
        for i in nums:
            sums += i
            minnum = min(sums, minnum)
        return 1 if minnum >= 0 else -minnum + 1


arr1 = [1,2]

t1 = datetime.now()
s = Solution()
print(s.minStartValue(arr1))
t2 = datetime.now()
print(t2 - t1)
