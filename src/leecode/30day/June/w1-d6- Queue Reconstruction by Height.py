from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda item: (-item[0], item[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


a = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
s = Solution()

print(s.reconstructQueue(a))
