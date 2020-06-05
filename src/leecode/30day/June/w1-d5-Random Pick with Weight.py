from random import randint
from typing import List
from bisect import bisect_left, bisect
from itertools import accumulate
import operator


class Solution:

    def __init__(self, w: List[int]):
        self.sums = list(accumulate(w, operator.add))
        self.x = self.sums[-1] - 1

    def pickIndex(self) -> int:
        z = randint(0, self.x)
        return bisect(self.sums, z)


a = [2, 7, 7, 9, 23]
y = accumulate(a, operator.add)
s = Solution(a)
s.pickIndex()


