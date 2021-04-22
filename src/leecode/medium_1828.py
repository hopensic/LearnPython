import math
from datetime import datetime
from typing import List

'''
tag: ^1828 ^medium ^math
name: ^(Queries on Number of Points Inside a Circle)
'''


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        le = len(queries)
        res = [0] * le
        for idx, (x2, y2, r) in enumerate(queries):
            for x1, y1 in points:
                if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r:
                    res[idx] += 1

        return res


points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]

t1 = datetime.now()
s = Solution()
print(s.countPoints(points, queries))
t2 = datetime.now()
print(t2 - t1)
