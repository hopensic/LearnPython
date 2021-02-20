from datetime import datetime
from typing import List

'''
tag: ^1557 ^medium ^graph
name: ^(Minimum Number of Vertices to Reach All Nodes)
'''


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        lst = [0] * n

        for _, d in edges:
            lst[d] += 1
        res = []
        for idx, i in enumerate(lst):
            if i == 0:
                res.append(idx)
        return res


n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]

t1 = datetime.now()
s = Solution()
print(s.findSmallestSetOfVertices(n, edges))
t2 = datetime.now()
print(t2 - t1)
