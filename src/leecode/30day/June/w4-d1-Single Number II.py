from functools import reduce
from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once


# nums = [0, 1, 0, 1, 0, 1, 99]
nums = [1, 1, 1, 2, 0, 1, 99]
so = Solution()
print(so.singleNumber(nums))
