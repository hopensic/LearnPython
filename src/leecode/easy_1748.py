from datetime import datetime
from typing import List

'''
tag: ^1748 ^easy ^array ^hash-table
name: ^(Sum of Unique Elements)
'''


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        set1 = set()
        res = 0
        subtract=set()
O        for i in nums:
            if i in set1:
                subtract.add(i)
            else:
                res += i
            set1.add(i)


        return res-sum(subtract)


arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]

t1 = datetime.now()
s = Solution()
print(s.sumOfUnique(arr1))
t2 = datetime.now()
print(t2 - t1)
