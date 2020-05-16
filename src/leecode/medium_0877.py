from datetime import datetime
from typing import List

'''
tag: ^877 ^medium ^math ^dp
name: ^(Stone Game)
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        def fun(start: int, end: int):
            if end - start == 1:
                return max(piles[start], piles[end])

            k = end - start
            #  如果k是偶数，返回最小值，如果k是奇数，返回最大值
            if k % 2 == 0:
                return min(fun(start, end - 1),
                           fun(start + 1, end))
            else:
                return max(piles[start] + fun(start + 1, end),
                           piles[end] + fun(start, end - 1))

        t = sum(piles)
        print(t)

        return fun(0, len(piles) - 1) > sum(piles) / 2


arr1 = [7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11,
        50, 16, 50, 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42, 46, 24]

t1 = datetime.now()
s = Solution()
print(s.stoneGame(arr1))
t2 = datetime.now()
print(t2 - t1)
