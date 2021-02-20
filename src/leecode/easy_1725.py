from datetime import datetime
from typing import List

'''
tag: ^1725 ^easy ^greedy
name: ^(Number Of Rectangles That Can Form The Largest Square)
'''


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        k = 0
        for lst in rectangles:
            t = min(lst)
            if t > k:
                res = 1
                k = t
            elif t == k:
                res += 1

        return res


arr1 = [[5,8],[3,9],[5,12],[16,5]]

t1 = datetime.now()
s = Solution()
print(s.countGoodRectangles(arr1))
t2 = datetime.now()
print(t2 - t1)
