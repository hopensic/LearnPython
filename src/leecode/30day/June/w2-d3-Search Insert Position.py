from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        d = bisect_left(nums, target)
        return d


nums = [1, 3, 5, 6]
target =99
s1 = Solution()
print(s1.searchInsert(nums, target))
