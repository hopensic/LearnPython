from collections import Counter, defaultdict
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while True:
            if start == end:
                return nums[start]
            mid_index = int((start + end) / 2)
            pre_index = mid_index - 1
            after_index = mid_index + 1

            m = nums[mid_index]
            pre = nums[pre_index]
            after = nums[after_index]
            if pre < m < after:
                return m
            if end - start == 2:
                return after if pre == m else pre
            if pre == m:
                if (end - after_index) % 2 == 1:
                    end = mid_index
                else:
                    start = after_index
            else:
                if (pre_index - start) % 2 == 1:
                    start = mid_index
                else:
                    end = pre_index


arr = [4,1, 1, 2, 2, 3, 3]
s1 = Solution()
print(s1.singleNonDuplicate(arr))
