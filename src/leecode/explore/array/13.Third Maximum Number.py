from collections import Counter
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        le = len(nums)
        if le == 2:
            return max(nums[0], nums[1])
        nums.sort(reverse=True)
        candicate = nums[0]
        n = 2
        i = 1
        while i < le and nums[i] <= nums[i - 1]:
            if n == 0:
                return nums[i - 1]
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            n -= 1
            i += 1
        return candicate if n > 0 else nums[i - 1]


nums = [2, 2, 3, 1]
solution = Solution()
print(solution.thirdMax(nums))
