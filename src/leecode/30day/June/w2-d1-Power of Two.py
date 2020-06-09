from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 if n > 0 else False


n = 3
s = Solution()
print(s.isPowerOfTwo(n))
