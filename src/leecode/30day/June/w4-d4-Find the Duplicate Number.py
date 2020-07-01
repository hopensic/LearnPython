from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            k = i * (-1 if i < 0 else 1)
            if nums[k - 1] < 0:
                return k
            else:
                nums[k - 1] *= -1


nums = [1, 3, 4, 2, 4]
# nums = [3, 1, 3, 4, 2]
# nums = [2, 2, 2, 2, 2]

so = Solution()
print(so.findDuplicate(nums))
