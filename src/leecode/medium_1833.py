from datetime import datetime
from typing import List

'''
tag: ^1833 ^medium ^array ^sort
name: ^(Maximum Ice Cream Bars)
'''


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        total = 0
        for i in costs:
            total += i
            if total > coins:
                return res
            else:
                res += 1

        return res


costs = [10,6,8,7,7,8]
coins =5

t1 = datetime.now()
s = Solution()
print(s.maxIceCream(costs, coins))
t2 = datetime.now()
print(t2 - t1)
