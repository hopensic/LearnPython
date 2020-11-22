from datetime import datetime
from typing import List

'''
tag: ^1561 ^medium ^sort
name: ^(Maximum Number of Coins You Can Get)
'''


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        return sum(piles[1:2 * n:2])


piles = [9,8,7,6,5,1,2,3,4]

t1 = datetime.now()
s = Solution()
print(s.maxCoins(piles))
t2 = datetime.now()
print(t2 - t1)
