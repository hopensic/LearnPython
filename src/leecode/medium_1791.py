from datetime import datetime
from typing import List

'''
tag: ^1791 ^medium ^graph
name: ^(Find Center of Star Graph)
'''


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a1, a2 = edges[0]
        b1, b2 = edges[1]

        if a1 == b1 or a1 == b2:
            return a1
        else:
            return a2


edges = [[1, 2], [2, 3], [4, 2]]

t1 = datetime.now()
s = Solution()
print(s.findCenter(edges))
t2 = datetime.now()
print(t2 - t1)
