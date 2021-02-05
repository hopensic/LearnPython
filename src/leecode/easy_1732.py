from datetime import datetime
from typing import List

'''
tag: ^1732 ^easy ^array
name: ^(Find the Highest Altitude)
'''


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        sums = 0
        for i in gain:
            sums += i
            if sums > res:
                res = sums

        return res


gain = [-4,-3,-2,-1,4,3,2]

t1 = datetime.now()
s = Solution()
print(s.largestAltitude(gain))
t2 = datetime.now()
print(t2 - t1)
