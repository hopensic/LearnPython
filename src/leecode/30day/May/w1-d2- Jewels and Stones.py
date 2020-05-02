from collections import Counter
from datetime import datetime


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(J.count,S))






J = "aA"
S = "aAAbbbb"
t1 = datetime.now()
s = Solution()
print(s.numJewelsInStones(J, S))
t2 = datetime.now()
print(t2 - t1)
