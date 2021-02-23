from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1742 ^easy ^array
name: ^(Maximum Number of Balls in a Box)
'''


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        m = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            m[sum(int(t) for t in str(i))] += 1
        return max(m.values())


lowLimit = 1
highLimit = 10

t1 = datetime.now()
s = Solution()
print(s.countBalls(lowLimit, highLimit))
t2 = datetime.now()
print(t2 - t1)
