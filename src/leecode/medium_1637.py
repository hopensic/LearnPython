from datetime import datetime
from typing import List

'''
tag: ^1637 ^medium ^sort
name: ^(Widest Vertical Area Between Two Points Containing No Points)
'''


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxnum = -1
        lst = sorted([d[0] for d in points])
        le = len(lst)
        for i in range(1, le):
            d = lst[i] - lst[i - 1]
            maxnum = d if d >= maxnum else maxnum
        return maxnum


arr1 = [[8,7],[9,9],[7,4],[9,7]]

t1 = datetime.now()
s = Solution()
print(s.maxWidthOfVerticalArea(arr1))
t2 = datetime.now()
print(t2 - t1)
