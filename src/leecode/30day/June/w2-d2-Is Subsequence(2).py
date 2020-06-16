from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        # t = iter(t)
        # return all(c in t for c in s)

        remainder_of_t = iter(t)
        # print(next(remainder_of_t))

        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True


s = "abc"
t = "ahbabgdc"
s1 = Solution()
print(s1.isSubsequence(s, t))
