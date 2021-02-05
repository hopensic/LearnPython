from datetime import datetime
from typing import List

'''
tag: ^1688 ^easy ^backtracking
name: ^(Count of Matches in Tournament)
'''


class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            x = n // 2
            res += x
            n = x if n % 2 == 0 else x + 1
        return res


t = 7

t1 = datetime.now()
s = Solution()
print(s.numberOfMatches(t))
t2 = datetime.now()
print(t2 - t1)
