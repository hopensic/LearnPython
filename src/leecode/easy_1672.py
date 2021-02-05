from datetime import datetime
from typing import List

'''
tag: ^1672 ^easy ^array
name: ^(Richest Customer Wealth)
'''


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])


arr1 = [[1, 5], [7, 3], [3, 5]]

t1 = datetime.now()
s = Solution()
print(s.maximumWealth(arr1))
t2 = datetime.now()
print(t2 - t1)
