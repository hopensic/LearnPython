from datetime import datetime
from typing import List

'''
tag: ^877 ^medium ^math ^dp
name: ^(Stone Game)
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dic = {}
        def fun(start: int, end: int):
            if end - start == 1:
                t = dic.get((start, end), max(piles[start], piles[end]))
                return t

            k = end - start
            #  如果k是偶数，返回最小值，如果k是奇数，返回最大值
            if k % 2 == 0:
                return min(dic[(start, end - 1)],
                           dic[(start + 1, end)])
            else:
                return max(piles[start] + dic[(start + 1, end)],
                           piles[end] + dic[(start, end - 1)])

        for i in range(1, len(piles)):
            for j in range(i - 1, -1, -1):
                dic[(j, i)] = fun(j, i)

        return dic[(0, len(piles) - 1)] > sum(piles) / 2


arr1 = [7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30, 27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4, 17, 11,
        50, 16, 50, 38, 34, 48, 27, 16, 24, 22, 48, 50, 10, 26, 27, 9, 43, 13, 42, 46, 24]

t1 = datetime.now()
s = Solution()
print(s.stoneGame(arr1))
t2 = datetime.now()
print(t2 - t1)
